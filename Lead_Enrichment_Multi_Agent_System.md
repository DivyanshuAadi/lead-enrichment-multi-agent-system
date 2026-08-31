# Lead Qualification & Enrichment Multi-Agent System (Meta Ads Library)

## 1. Executive Summary & System Architecture

The **Lead Qualification & Enrichment Multi-Agent System** is an enterprise-grade, distributed agentic framework designed to transform unnormalized Facebook Meta Ads Library exports into ranked, high-converting B2B outreach battlecards.

Built on an asynchronous supervisor-worker pattern, the system combines:
1. **Dynamic Workload Sharding**: Automatically partitions deduplicated leads across parallel worker pods based on real-time hardware constraints and SLA requirements.
2. **Concurrency Throttling (`asyncio.Semaphore(4)`)**: Prevents IP rate-limiting, proxy bans, and Playwright headless browser crashes by enforcing 4 concurrent workers per pod.
3. **Multi-Modal Forensic Auditing**: Runs dual-branch parallel investigation combining Deep Research (creative angles, ad spend modeling, leakage estimation) with Headless Browser Automation (Core Web Vitals, mobile CRO, CAPI/Pixel tag detection, Google Maps, Instagram, WhatsApp widgets).
4. **4-Pillar Algorithmic Qualification**: Calculates a composite lead score (0–100) and classifies leads into Tier A (Hot), Tier B (Warm), and Tier C (Unqualified).
5. **Jeremy Miner NEPQ (Neuro-Emotional Persuasion Questioning) Behavioral Outbound Synthesis**: Automatically drafts 4-part cold call openers, situation/problem awareness probes, and 3-step objection handlers for sales reps.

---

## 2. Phase 1: CEO Ingestion, Deduplication & Interactive Sharding

### 2.1 Deduplication Algorithm
Raw Meta Ads Library exports contain redundant, multi-row ad listings per advertiser entity. The CEO Agent parses the raw CSV, clusters listings by canonical `page_id` and domain, and transforms them into an array of deduplicated business objects containing two fundamental sub-components:
1. `Common_Info_Found_Among_Ads`: Shared infrastructure, advertiser metadata, aggregated monthly spend brackets, and omni-channel footprint.
2. `Ads`: An array of individual ad creatives running under that business entity.

---

## 3. Phase 2 & 3: Inside the Manager Pod Architecture

### 3.1 Manager Pod Supervisor (`engineering-multi-agent-systems-architect`)
- **Concurrency Throttling:** Enforces `asyncio.Semaphore(4)` per pod to prevent rate-limit bans and Playwright memory exhaustion.
- **Error Isolation Boundary:** Wraps all worker operations in resilient try/except sandboxes. If a prospect website fails to resolve (DNS error, Cloudflare block, 404), the error is isolated, baseline data is logged, and execution continues without crashing sibling tasks.

### 3.2 Stream 1: Deep Research & Revenue Intelligence Agents
1. **✍️ Ad Creative Strategist (`paid-media-creative-strategist.md`)**: Parses ad copy, headlines, visual hooks, emotional angles, and UVP.
2. **📊 Paid Media Auditor (`paid-media-auditor.md`)**: Models monthly impression volume, estimated CPM, monthly ad spend bracket ($/mo).
3. **📈 Paid Social Strategist (`paid-media-paid-social-strategist.md`)**: Evaluates multi-platform balance and creative fatigue.
4. **📸 Instagram Curator & Social Strategist (`marketing-instagram-curator.md`)**: Audits organic social proof.

### 3.3 Stream 2: Vision & Browser Audit Agents (Headless Playwright Automation)
1. **🎭 Persona Walkthrough Specialist (`design-persona-walkthrough.md`)**: Emulates mobile user journey.
2. **⚡ Web Performance Engineer (`engineering-wordpress-performance.md`)**: Analyzes Core Web Vitals: LCP, CLS, FID.
3. **📡 Tracking & Measurement Specialist (`paid-media-tracking-specialist.md`)**: Inspects Meta Pixel & CAPI.
4. **🌐 Multi-Touchpoint Browser Scanner**: Verifies Google Maps and instant chat widgets.

### 3.4 Stage 3: Algorithmic Qualification Agent
- **Pillar 1**: Financial Capacity (35%)
- **Pillar 2**: Technical Friction Leakage (30%)
- **Pillar 3**: Offer & Messaging Congruence (20%)
- **Pillar 4**: Omnichannel Accessibility (15%)

### 3.5 Stage 4: Jeremy Miner NEPQ Sales Hook Agent
Synthesizes 4-part cold call scripts:
1. Pattern Interrupt Opener (No commission breath)
2. Situation Question (Context anchor)
3. Problem Awareness Probe (Forensic friction probe)
4. Solution Bridge & Non-Pushy Pitch
5. 3-Step Objection Annihilation Loops (In-House Team, Budget, Send Email)

---

## 4. Summary of Agency Agent Roles

| Pod Phase | Agent Role | Source File | Responsibilities |
|---|---|---|---|
| **Pod Supervisor** | Multi-Agent Architect | `engineering-multi-agent-systems-architect.md` | `asyncio.Semaphore(4)`, Error Isolation Sandbox |
| **Stream 1: Research** | Ad Creative Strategist | `paid-media-creative-strategist.md` | Hooks, angles, emotional resonance |
| **Stream 1: Research** | Paid Media Auditor | `paid-media-auditor.md` | Impressions, monthly spend, leakage |
| **Stream 1: Research** | Paid Social Strategist | `paid-media-paid-social-strategist.md` | Multi-platform allocation |
| **Stream 1: Research** | Instagram Curator | `marketing-instagram-curator.md` | Social proof & feed audit |
| **Stream 2: Vision** | Persona Walkthrough | `design-persona-walkthrough.md` | Headless mobile UX journey |
| **Stream 2: Vision** | Performance Engineer | `engineering-wordpress-performance.md` | Core Web Vitals (LCP, FID, CLS) |
| **Stream 2: Vision** | Tracking Specialist | `paid-media-tracking-specialist.md` | Meta Pixel, CAPI, GTM |
| **Stream 2: Vision** | Multi-Touchpoint Scanner | Custom Worker | Maps, WhatsApp widgets |
| **Stage 3: Qualification** | Deal Strategist | `sales-deal-strategist.md` | Dynamic Qualification scoring |
| **Stage 4: NEPQ Sales** | Discovery Coach | `sales-discovery-coach.md` | Situation & Problem awareness |
| **Stage 4: NEPQ Sales** | Outbound Strategist | `sales-outbound-strategist.md` | 4-part cold call hook |
| **Stage 4: NEPQ Sales** | Offer & Lead Gen | `sales-offer-lead-gen.md` | 3-step objection handlers |
