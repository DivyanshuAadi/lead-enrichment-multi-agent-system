"""Stage 1: Deep Research & Revenue Intelligence Stream.
Agency Agents:
- Creative Strategist (paid-media-creative-strategist.md)
- Paid Media Auditor (paid-media-auditor.md)
- Paid Social Strategist (paid-media-paid-social.md)
- Instagram Curator (marketing-instagram-curator.md)
"""
from models import DeduplicatedBusiness, ResearchIntel

class DeepResearchStream:
    """Performs deep research on ad copy, spend modeling, and revenue leakage."""

    @staticmethod
    async def run(business: DeduplicatedBusiness) -> ResearchIntel:
        ads = business.Ads
        total_ads = len(ads)

        # 1. Creative Hook Analysis
        hooks = [ad.headline for ad in ads if ad.headline]
        copy_angles = list(set([ad.cta_type for ad in ads if ad.cta_type]))
        primary_promise = hooks[0] if hooks else "High ROI Service Offering"

        # 2. Revenue & Spend Modeling
        # Formula: $850/mo baseline spend per active ad set
        est_monthly_spend = total_ads * 850

        # Wasted Ad Spend Leakage Model:
        # If running >= 3 ads without varied angles, estimate 22-35% ad fatigue leakage
        leakage_rate = 0.28 if total_ads >= 3 else 0.15
        wasted_spend = int(est_monthly_spend * leakage_rate)

        # 3. Fatigue & Scalability Flags
        fatigue_risk = "HIGH" if total_ads >= 4 else ("MEDIUM" if total_ads >= 2 else "LOW")
        scalability = "READY_TO_SCALE" if est_monthly_spend >= 2500 else "NEEDS_OPTIMIZATION"

        return ResearchIntel(
            est_monthly_spend_usd=est_monthly_spend,
            active_campaign_count=max(1, total_ads // 2),
            core_hooks=hooks[:3],
            primary_promise=primary_promise,
            ad_copy_angles=copy_angles,
            wasted_ad_spend_leakage_usd=wasted_spend,
            creative_fatigue_risk=fatigue_risk,
            scalability_verdict=scalability
        )
