"""Manager Pod Supervisor Agent.
Agency Agent: Multi-Agent Systems Architect (engineering-multi-agent-systems-architect.md)

Responsibilities:
1. Coordinates Stream 1 (Deep Research) & Stream 2 (Vision/Browser) in parallel per lead.
2. Evaluates Qualification Stage 3 against Qualification.md.
3. Invokes Stage 4 NEPQ Sales Hook for Tier A/B qualified leads.
4. Enforces asyncio.Semaphore(4) concurrency throttling.
5. Implements per-lead try/except error boundary sandbox.
"""
import asyncio
import logging
from typing import List
from models import DeduplicatedBusiness, EnrichedLead
from agents.deep_research import DeepResearchStream
from agents.vision_browser import VisionBrowserStream
from agents.qualification import QualificationAgent
from agents.nepq_sales_hook import NEPQSalesHookAgent

logger = logging.getLogger("ManagerPodSupervisor")

class ManagerPod:
    """Isolated concurrent execution pod managing a shard of deduplicated leads."""

    def __init__(self, pod_id: int, leads: List[DeduplicatedBusiness], enable_nepq: bool = True, concurrency_limit: int = 4):
        self.pod_id = pod_id
        self.leads = leads
        self.enable_nepq = enable_nepq
        self.semaphore = asyncio.Semaphore(concurrency_limit)

    async def _process_single_lead(self, business: DeduplicatedBusiness) -> EnrichedLead:
        """Processes one lead through the full multi-agent pipeline within an error boundary."""
        async with self.semaphore:
            try:
                logger.info(f"[Pod {self.pod_id}] Starting audit: {business.businessName}")

                # Parallel Stream 1 & Stream 2
                research, vision = await asyncio.gather(
                    DeepResearchStream.run(business),
                    VisionBrowserStream.run(business)
                )

                # Stage 3: Dynamic Qualification
                qualification = QualificationAgent.evaluate(business, research, vision)

                # Stage 4: Jeremy Miner NEPQ Battlecard
                nepq_card = None
                if self.enable_nepq and qualification.is_qualified_for_nepq:
                    nepq_card = NEPQSalesHookAgent.generate(business, research, vision, qualification)

                # Compile Unified Enriched Record
                enriched = EnrichedLead(
                    business_name=business.businessName,
                    page_id=business.Common_Info_Found_Among_Ads.get("page_id", ""),
                    canonical_domain=business.Common_Info_Found_Among_Ads.get("canonical_domain", ""),
                    primary_category=business.Common_Info_Found_Among_Ads.get("primary_category", "General"),
                    total_active_ads=len(business.Ads),
                    estimated_monthly_spend_usd=research.est_monthly_spend_usd,
                    wasted_ad_spend_leakage_usd=research.wasted_ad_spend_leakage_usd,
                    qualification_score=qualification.qualification_score,
                    lead_tier=qualification.lead_tier,
                    primary_friction_point=qualification.primary_friction_point,
                    mobile_lcp_sec=vision.lcp_sec,
                    meta_capi_status=vision.capi_status,
                    nepq_pattern_interrupt=nepq_card.pattern_interrupt if nepq_card else None,
                    nepq_situation_question=nepq_card.situation_question if nepq_card else None,
                    nepq_problem_awareness_probe=nepq_card.problem_awareness_probe if nepq_card else None,
                    nepq_solution_bridge_pitch=nepq_card.solution_bridge_pitch if nepq_card else None,
                    objection_inhouse_team=nepq_card.objection_inhouse_team if nepq_card else None,
                    objection_budget=nepq_card.objection_budget if nepq_card else None,
                    objection_send_email=nepq_card.objection_send_email if nepq_card else None
                )
                logger.info(f"[Pod {self.pod_id}] Completed {business.businessName} -> Score: {qualification.qualification_score} ({qualification.lead_tier})")
                return enriched

            except Exception as exc:
                # Per-lead Fault Isolation Boundary
                logger.error(f"[Pod {self.pod_id}] Error processing {business.businessName}: {exc}", exc_info=True)
                return EnrichedLead(
                    business_name=business.businessName,
                    page_id=business.Common_Info_Found_Among_Ads.get("page_id", ""),
                    canonical_domain=business.Common_Info_Found_Among_Ads.get("canonical_domain", ""),
                    primary_category="Error / Unprocessed",
                    total_active_ads=len(business.Ads),
                    estimated_monthly_spend_usd=0,
                    wasted_ad_spend_leakage_usd=0,
                    qualification_score=0,
                    lead_tier="Tier C (Unqualified)",
                    primary_friction_point=f"Execution Error: {str(exc)[:60]}",
                    mobile_lcp_sec=0.0,
                    meta_capi_status="Unknown"
                )

    async def execute_shard(self) -> List[EnrichedLead]:
        """Executes all leads assigned to this Manager Pod."""
        logger.info(f"[Pod {self.pod_id}] Executing shard of {len(self.leads)} leads with Semaphore(4)")
        tasks = [self._process_single_lead(lead) for lead in self.leads]
        return await asyncio.gather(*tasks)
