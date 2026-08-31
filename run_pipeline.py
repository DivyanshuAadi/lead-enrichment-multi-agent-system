"""Pipeline CLI Runner."""
import sys
import asyncio
import logging
from ceo_orchestrator import CEOOrchestrator

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except AttributeError:
        pass

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(name)s: %(message)s")

async def main():
    csv_file = "sample_meta_ads.csv"
    output_file = "Clean_Enriched_Leads.csv"

    print("=================================================================")
    print("🚀 LAUNCHING LEAD ENRICHMENT MULTI-AGENT SYSTEM")
    print("=================================================================")

    ceo = CEOOrchestrator(target_shard_size=3, concurrency_limit_per_pod=4)
    leads = await ceo.run_pipeline(csv_file, output_file)

    print("\n=================================================================")
    print("🎯 EXECUTION COMPLETE — TOP QUALIFIED LEADS")
    print("=================================================================")
    for lead in leads[:3]:
        print(f"\n🏢 {lead.business_name} (Score: {lead.qualification_score} - {lead.lead_tier})")
        print(f"   💸 Estimated Spend: ${lead.estimated_monthly_spend_usd:,}/mo | Leakage: ${lead.wasted_ad_spend_leakage_usd:,}/mo")
        print(f"   ⚠️ Primary Friction: {lead.primary_friction_point}")
        if lead.nepq_pattern_interrupt:
            print(f"   📞 NEPQ Opener: \"{lead.nepq_pattern_interrupt}\"")

if __name__ == "__main__":
    asyncio.run(main())
