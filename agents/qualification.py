"""Stage 3: Algorithmic Qualification Agent.
Agency Agents:
- Deal Strategist (sales-deal-strategist.md)
- Paid Social Strategist (paid-media-paid-social.md)

Evaluates leads dynamically based on Qualification.md specifications:
1. Financial Capacity & Ad Spend Viability (Weight: 35%)
2. Technical & Funnel Friction Leakage (Weight: 30%)
3. Offer & Messaging Market Congruence (Weight: 20%)
4. Decision-Maker Accessibility & Trajectory (Weight: 15%)
"""
from typing import Optional, Dict, Any
from models import DeduplicatedBusiness, ResearchIntel, VisionIntel, QualificationResult
from agents.qualification_parser import QualificationSpecParser

class QualificationAgent:
    """Calculates composite qualification score (0-100) and assigns tier based on Qualification.md."""

    _cached_spec: Optional[Dict[str, Any]] = None

    @classmethod
    def get_spec(cls, spec_path: str = "Qualification.md") -> Dict[str, Any]:
        if cls._cached_spec is None:
            cls._cached_spec = QualificationSpecParser.load_spec(spec_path)
        return cls._cached_spec

    @classmethod
    def evaluate(
        cls,
        business: DeduplicatedBusiness,
        research: ResearchIntel,
        vision: VisionIntel,
        spec: Optional[Dict[str, Any]] = None
    ) -> QualificationResult:
        active_spec = spec or cls.get_spec()
        min_spend = active_spec.get("min_monthly_spend", 2500)
        max_lcp = active_spec.get("max_lcp_sec", 3.5)

        # Pillar 1: Financial Capacity (0-100)
        spend = research.est_monthly_spend_usd
        if spend >= (min_spend * 2.5):
            p1 = 100.0
        elif spend >= (min_spend * 1.5):
            p1 = 85.0
        elif spend >= min_spend:
            p1 = 65.0
        else:
            p1 = 30.0

        # Pillar 2: Technical Friction Leakage (0-100)
        p2 = 40.0
        if vision.lcp_sec > max_lcp:
            p2 += 30.0
        elif vision.lcp_sec > 2.8:
            p2 += 15.0

        if vision.capi_status == "Missing":
            p2 += 30.0
        elif vision.capi_status == "Inactive":
            p2 += 15.0

        p2 = min(100.0, p2)

        # Pillar 3: Offer & Messaging Congruence (0-100)
        p3 = 75.0 if len(research.ad_copy_angles) > 1 else 50.0

        # Pillar 4: Accessibility & Omnichannel Presence (0-100)
        p4 = 50.0
        if vision.has_whatsapp_widget:
            p4 += 25.0
        if vision.total_maps_reviews > 20:
            p4 += 25.0
        p4 = min(100.0, p4)

        # Composite Weighted Score
        composite_score = int(round(
            (0.35 * p1) +
            (0.30 * p2) +
            (0.20 * p3) +
            (0.15 * p4)
        ))

        # Assign Tier
        if composite_score >= 80:
            tier = "Tier A (Hot)"
            qual_nepq = True
        elif composite_score >= 60:
            tier = "Tier B (Warm)"
            qual_nepq = True
        else:
            tier = "Tier C (Unqualified)"
            qual_nepq = False

        # Identify dominant friction point
        frictions = []
        if vision.lcp_sec > max_lcp:
            frictions.append(f"Slow Mobile LCP ({vision.lcp_sec}s)")
        if vision.capi_status in ["Missing", "Inactive"]:
            frictions.append(f"Meta CAPI {vision.capi_status}")
        if not vision.has_whatsapp_widget:
            frictions.append("Missing Instant Chat Widget")
        if not frictions:
            frictions.append("Creative Fatigue & Ad Spend Inefficiency")

        dominant_friction = " + ".join(frictions[:2])

        return QualificationResult(
            qualification_score=composite_score,
            lead_tier=tier,
            pillar_scores={"P1_Financial": p1, "P2_Friction": p2, "P3_Offer": p3, "P4_Access": p4},
            primary_friction_point=dominant_friction,
            is_qualified_for_nepq=qual_nepq
        )
