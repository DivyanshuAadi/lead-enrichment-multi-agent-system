"""Stage 4: Jeremy Miner NEPQ Sales Hook Generator.
Agency Agents:
- Discovery Coach (sales-discovery-coach.md)
- Outbound Strategist (sales-outbound-strategist.md)
- Offer Lead Gen (sales-offer-lead-gen.md)

Constructs:
1. Pattern Interrupt Opener (Neutral, curious tonality, no commission breath)
2. Situation Question (Anchors on active ad count and estimated spend)
3. Problem Awareness Probe (Pinpoints forensic technical friction)
4. Solution Bridge Pitch (Non-pushy offer to share diagnostic findings)
5. 3-Step Objection Loops (Defuse -> Isolate -> Reframe)
"""
from models import DeduplicatedBusiness, ResearchIntel, VisionIntel, QualificationResult, NEPQBattlecard

class NEPQSalesHookAgent:
    """Synthesizes high-conversion psychological sales hooks and objection loops."""

    @staticmethod
    def generate(
        business: DeduplicatedBusiness,
        research: ResearchIntel,
        vision: VisionIntel,
        qualification: QualificationResult
    ) -> NEPQBattlecard:
        name = business.businessName
        ads_count = len(business.Ads)
        spend = f"${research.est_monthly_spend_usd:,}"
        leakage = f"${research.wasted_ad_spend_leakage_usd:,}"
        friction = qualification.primary_friction_point

        # 1. Pattern Interrupt (Zero Commission Breath)
        pattern_interrupt = (
            f"Hey [First Name], I noticed {name} is running {ads_count} live Meta campaigns right now—"
            f"not reaching out to pitch ad management, just had a quick diagnostic question about your landing page routing..."
        )

        # 2. Situation Question
        situation_q = (
            f"Given that your team is investing approximately {spend}/month across {ads_count} active ad sets, "
            f"who is currently overseeing mobile conversion telemetry and post-click tracking?"
        )

        # 3. Problem Awareness Probe
        problem_probe = (
            f"When we ran a headless audit on your top creative landing page, we detected a {vision.lcp_sec}s Mobile LCP "
            f"and unconfigured Meta CAPI, resulting in an estimated {leakage}/mo in untracked drop-offs. "
            f"Are you guys aware that mobile traffic might be bouncing before the page even renders?"
        )

        # 4. Solution Bridge Pitch
        solution_pitch = (
            f"We put together a 2-minute video breakdown of the exact friction bottlenecks and how to recover that {leakage}/mo. "
            f"Would you be against me sending that over for your dev or media team to look at?"
        )

        # 5. Objection Handlers
        obj_inhouse = (
            "Step 1 (Defuse): 'Totally understand, most established brands have a dedicated media buyer.' "
            "Step 2 (Isolate): 'Is your in-house team primarily focused on creative production, or server-side telemetry?' "
            "Step 3 (Reframe): 'This audit is purely technical—we hand the diagnostic findings directly to your team so they can plug the leakage without changing your setup.'"
        )

        obj_budget = (
            "Step 1 (Defuse): 'That makes complete sense—budgets are tight across paid acquisition.' "
            "Step 2 (Isolate): 'If the {leakage}/mo leakage wasn't happening, would exploring conversion recovery make sense?' "
            "Step 3 (Reframe): 'Our optimization pays for itself from recovered ad spend alone before any retainer.'"
        )

        obj_email = (
            "Step 1 (Defuse): 'Happy to do that so you can review at your own pace.' "
            "Step 2 (Isolate): 'What's the best email address where you actually check audit attachments?' "
            "Step 3 (Reframe): 'I'll send the 2-minute Loom now. If you see value, we can chat for 5 mins later this week.'"
        )

        return NEPQBattlecard(
            pattern_interrupt=pattern_interrupt,
            situation_question=situation_q,
            problem_awareness_probe=problem_probe,
            solution_bridge_pitch=solution_pitch,
            objection_inhouse_team=obj_inhouse,
            objection_budget=obj_budget,
            objection_send_email=obj_email
        )
