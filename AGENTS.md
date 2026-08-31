# AGENTS.md: Autonomous Multi-Agent Hierarchy & Topology

## 1. Multi-Agent Hierarchy

```
                               ┌────────────────────────────────┐
                               │   👑 CEO ORCHESTRATOR AGENT    │
                               │  - Dynamic Schema Synthesizer  │
                               │  - Shard Partitioner           │
                               │  - Model Router (Sonnet/Pro)   │
                               └───────────────┬────────────────┘
                                               │
                        ┌──────────────────────┴──────────────────────┐
                        ▼                                             ▼
          ┌───────────────────────────┐                 ┌───────────────────────────┐
          │     📦 MANAGER POD 1      │                 │     📦 MANAGER POD 2      │
          │  Supervisor (Semaphore:4) │                 │  Supervisor (Semaphore:4) │
          └─────────────┬─────────────┘                 └─────────────┬─────────────┘
                        │                                             │
          ┌─────────────┴─────────────┐                 ┌─────────────┴─────────────┐
          ▼                           ▼                 ▼                           ▼
  [Stream 1: Research]       [Stream 2: Vision]  [Stream 1: Research]       [Stream 2: Vision]
  (Haiku / Flash / Mini)     (Haiku / Flash)     (Haiku / Flash / Mini)     (Haiku / Flash)
  - Creative Strategist      - UX Walkthrough    - Creative Strategist      - UX Walkthrough
  - Paid Media Auditor       - Web Performance   - Paid Media Auditor       - Web Performance
  - Paid Social Strategist   - Tracking & CAPI   - Paid Social Strategist   - Tracking & CAPI
  - Instagram Curator        - Touchpoint Scan   - Instagram Curator        - Touchpoint Scan
          │                           │                 │                           │
          └─────────────┬─────────────┘                 └─────────────┬─────────────┘
                        │                                             │
                        ▼                                             ▼
          ┌───────────────────────────┐                 ┌───────────────────────────┐
          │  ♟️ QUALIFICATION AGENT   │                 │  ♟️ QUALIFICATION AGENT   │
          │  Follows Qualification.md │                 │  Follows Qualification.md │
          │    (Haiku / Flash / Mini) │                 │    (Haiku / Flash / Mini) │
          └─────────────┬─────────────┘                 └─────────────┬─────────────┘
                        │ (If Tier A / B)                             │ (If Tier A / B)
                        ▼                                             ▼
          ┌───────────────────────────┐                 ┌───────────────────────────┐
          │ 🎯 JEREMY MINER NEPQ HOOK │                 │ 🎯 JEREMY MINER NEPQ HOOK │
          │ 4-Stage Behavioral Script │                 │ 4-Stage Behavioral Script │
          │   (Flagship: Sonnet / Pro)│                 │   (Flagship: Sonnet / Pro)│
          └───────────────────────────┘                 └───────────────────────────┘
```

## 2. Agency Agents Role Definitions (from `msitarzewski/agency-agents`)

1. **Manager Pod Supervisor**: `engineering-multi-agent-systems-architect.md`
   - Coordinates the sub-agent DAG, enforces `asyncio.Semaphore(4)` concurrency throttling, and isolates failure boundaries.
2. **Creative & Pain-Point Strategist**: `paid-media-creative-strategist.md`
   - Deconstructs emotional angles, core promises, hooks, and CTA clarity from raw ad creatives.
3. **Revenue & Ad Spend Auditor**: `paid-media-auditor.md`
   - Models monthly impressions, estimated ad spend brackets, and quantifies wasted ad leakage ($/mo).
4. **Social & Organic Alignment Curator**: `marketing-instagram-curator.md` + `paid-media-paid-social-strategist.md`
   - Audits multi-platform distribution (FB/IG) and verifies organic bio and grid congruence.
5. **Headless UX & Conversion Auditor**: `design-persona-walkthrough.md`
   - Audits mobile landing page experience, CTA visibility, and form completion friction.
6. **Web Performance & Core Web Vitals Engineer**: `engineering-wordpress-performance.md`
   - Measures Mobile Largest Contentful Paint (LCP), FID, CLS, and page rendering bottlenecks.
7. **Tracking & Server-Side Telemetry Specialist**: `paid-media-tracking-specialist.md`
   - Inspects Meta Pixel, Conversions API (CAPI), and Google Tag Manager health.
8. **Qualification Deal Strategist**: `sales-deal-strategist.md`
   - Evaluates leads strictly against `Qualification.md` criteria (0–100 score).
9. **Jeremy Miner NEPQ Sales Hook Coach**: `sales-discovery-coach.md` + `sales-outbound-strategist.md` + `sales-offer-lead-gen.md`
   - Synthesizes 4-part NEPQ cold call openers (Pattern Interrupt -> Situation -> Problem Awareness -> Non-Pushy Pitch) and 3-step objection handlers.
