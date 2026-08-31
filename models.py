"""Type-safe data schemas for Lead Enrichment Multi-Agent System."""
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional

@dataclass
class LeadAd:
    adId: str
    ad_archive_id: str
    headline: str
    body_copy: str
    cta_type: str
    destination_url: str
    spend_range_usd: Optional[str] = None
    impressions_range: Optional[str] = None

@dataclass
class DeduplicatedBusiness:
    businessName: str
    Common_Info_Found_Among_Ads: Dict[str, Any]
    Ads: List[LeadAd] = field(default_factory=list)

@dataclass
class ResearchIntel:
    est_monthly_spend_usd: int
    active_campaign_count: int
    core_hooks: List[str]
    primary_promise: str
    ad_copy_angles: List[str]
    wasted_ad_spend_leakage_usd: int
    creative_fatigue_risk: str
    scalability_verdict: str

@dataclass
class VisionIntel:
    lcp_sec: float
    fid_ms: int
    cls_score: float
    has_meta_pixel: bool
    capi_status: str
    ssl_status: str
    mobile_responsive: bool
    has_whatsapp_widget: bool
    total_maps_reviews: int
    maps_rating: float

@dataclass
class QualificationResult:
    qualification_score: int
    lead_tier: str
    pillar_scores: Dict[str, float]
    primary_friction_point: str
    is_qualified_for_nepq: bool

@dataclass
class NEPQBattlecard:
    pattern_interrupt: str
    situation_question: str
    problem_awareness_probe: str
    solution_bridge_pitch: str
    objection_inhouse_team: str
    objection_budget: str
    objection_send_email: str

@dataclass
class EnrichedLead:
    business_name: str
    page_id: str
    canonical_domain: str
    primary_category: str
    total_active_ads: int
    estimated_monthly_spend_usd: int
    wasted_ad_spend_leakage_usd: int
    qualification_score: int
    lead_tier: str
    primary_friction_point: str
    mobile_lcp_sec: float
    meta_capi_status: str
    nepq_pattern_interrupt: Optional[str] = None
    nepq_situation_question: Optional[str] = None
    nepq_problem_awareness_probe: Optional[str] = None
    nepq_solution_bridge_pitch: Optional[str] = None
    objection_inhouse_team: Optional[str] = None
    objection_budget: Optional[str] = None
    objection_send_email: Optional[str] = None
