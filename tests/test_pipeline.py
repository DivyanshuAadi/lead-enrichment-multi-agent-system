"""Unit and Integration tests for Lead Qualification & Enrichment Multi-Agent System."""
import pytest
import asyncio
import os
from deduplicator import CEODeduplicationEngine
from models import DeduplicatedBusiness, LeadAd
from agents.deep_research import DeepResearchStream
from agents.vision_browser import VisionBrowserStream
from agents.qualification import QualificationAgent
from agents.nepq_sales_hook import NEPQSalesHookAgent
from agents.supervisor import ManagerPod
from postprocessor import PostProcessor
from dynamic_code_generator import DynamicSchemaSynthesizer

@pytest.fixture
def sample_business():
    return DeduplicatedBusiness(
        businessName="Apex Growth Dental",
        Common_Info_Found_Among_Ads={
            "page_id": "109847101",
            "page_name": "Apex Growth Dental",
            "canonical_domain": "https://apexgrowthdental.com",
            "primary_category": "Dental & Aesthetics",
            "currency": "USD",
            "total_active_ads": 3,
            "estimated_monthly_spend_usd": 2850,
            "platforms_detected": ["facebook", "instagram"],
            "social_handles": {"whatsapp": "+1-800-555-0101"}
        },
        Ads=[
            LeadAd(
                adId="AD_101_1",
                ad_archive_id="ARC_101_1",
                headline="Get $500 Off Clear Aligners This Week",
                body_copy="Custom invisible aligners crafted by board-certified orthodontists.",
                cta_type="BOOK_NOW",
                destination_url="https://apexgrowthdental.com/aligners-promo"
            )
        ]
    )

def test_deduplication_clusters_ads():
    csv_file = "sample_meta_ads.csv"
    assert os.path.exists(csv_file)
    deduped = CEODeduplicationEngine.process_csv(csv_file)
    assert len(deduped) == 6  # 6 distinct businesses in sample dataset
    dental = next(d for d in deduped if "Apex Growth Dental" in d.businessName)
    assert len(dental.Ads) == 3
    assert dental.Common_Info_Found_Among_Ads["total_active_ads"] == 3

def test_dynamic_schema_synthesizer():
    csv_file = "sample_meta_ads.csv"
    schema = DynamicSchemaSynthesizer.inspect_csv_schema(csv_file)
    assert len(schema["headers"]) > 5
    assert schema["discovered_mapping"]["entity_col"] == "page_name"
    assert schema["discovered_mapping"]["url_col"] == "destination_url"
    custom_code = DynamicSchemaSynthesizer.generate_custom_parser_code(csv_file)
    assert "parse_custom_dataset" in custom_code
    assert "DeduplicatedBusiness" in custom_code

def test_deep_research_and_vision_streams(sample_business):
    async def _run():
        research, vision = await asyncio.gather(
            DeepResearchStream.run(sample_business),
            VisionBrowserStream.run(sample_business)
        )
        assert research.est_monthly_spend_usd > 0
        assert research.wasted_ad_spend_leakage_usd > 0
        assert vision.lcp_sec > 0
        assert vision.ssl_status == "Valid (HTTPS)"
    asyncio.run(_run())

def test_qualification_scoring(sample_business):
    async def _run():
        research, vision = await asyncio.gather(
            DeepResearchStream.run(sample_business),
            VisionBrowserStream.run(sample_business)
        )
        qual = QualificationAgent.evaluate(sample_business, research, vision)
        assert 0 <= qual.qualification_score <= 100
        assert qual.lead_tier in ["Tier A (Hot)", "Tier B (Warm)", "Tier C (Unqualified)"]
    asyncio.run(_run())

def test_nepq_sales_hook_generation(sample_business):
    async def _run():
        research, vision = await asyncio.gather(
            DeepResearchStream.run(sample_business),
            VisionBrowserStream.run(sample_business)
        )
        qual = QualificationAgent.evaluate(sample_business, research, vision)
        battlecard = NEPQSalesHookAgent.generate(sample_business, research, vision, qual)
        assert "Apex Growth Dental" in battlecard.pattern_interrupt
        assert "active ad sets" in battlecard.situation_question
        assert "drop-offs" in battlecard.problem_awareness_probe
        assert "diagnostic call" in battlecard.solution_bridge_pitch
        assert len(battlecard.objection_inhouse_team) > 20
    asyncio.run(_run())

def test_manager_pod_execution(sample_business):
    async def _run():
        pod = ManagerPod(pod_id=1, leads=[sample_business], enable_nepq=True)
        results = await pod.execute_shard()
        assert len(results) == 1
        lead = results[0]
        assert lead.business_name == "Apex Growth Dental"
        assert lead.qualification_score > 0
        assert lead.nepq_pattern_interrupt is not None
    asyncio.run(_run())

def test_postprocessor_dataframe_and_csv(sample_business):
    async def _run():
        pod = ManagerPod(pod_id=1, leads=[sample_business], enable_nepq=True)
        results = await pod.execute_shard()
        df = PostProcessor.compile_dataframe(results)
        assert len(df) == 1
        assert "rank" in df.columns
        assert df["rank"].iloc[0] == 1
        out_csv = PostProcessor.export_csv(results, "test_output.csv")
        assert os.path.exists(out_csv)
        if os.path.exists(out_csv):
            os.remove(out_csv)
    asyncio.run(_run())
