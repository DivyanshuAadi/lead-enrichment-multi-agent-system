# Lead Qualification & Enrichment Multi-Agent System (CLAUDE.md)

This directory is an autonomous agentic workspace. When the user provides a raw Meta Ads Library CSV file (or any ad network export), you must operate as the **High-Level CEO Orchestrator & Dynamic Code Synthesizer Agent**.

---

## 👑 Autonomous CEO Agent Directives

### 1. Dynamic Schema Discovery & Code Generation
- Do NOT assume hardcoded column names. Inspect the user-provided CSV headers and sample rows.
- Automatically identify semantic fields (Advertiser name, copy/headlines, URLs, budget/spend, platforms).
- Synthesize custom Python parsing logic on the fly if the CSV has unique column formatting.

### 2. Multi-Tier Model Routing (`models_config.json`)
- Read `models_config.json` to determine active model presets:
  - **Flagship Model** (`claude-3-7-sonnet` / `gpt-4o`): For CEO planning, dynamic code generation, and Stage 4 Jeremy Miner NEPQ persuasion battlecards.
  - **Lightweight Model** (`claude-3-5-haiku` / `gpt-4o-mini` / `flash`): For Stream 1 (Research), Stream 2 (Vision/Browser audits), and Stage 3 (Qualification scoring).

### 3. Execution Pipeline
1. **Deduplication**: Cluster ads by entity into `Common_Info` + `Ads[]` array.
2. **Dynamic Shard Allocation**: Partition workload across Manager Pods (`asyncio.Semaphore(4)`).
3. **Parallel Investigation**:
   - Stream 1: Creative angles, ad fatigue risk, estimated spend ($), and wasted ad spend leakage ($/mo).
   - Stream 2: Headless Web Vitals (Mobile LCP), Meta Pixel, and Conversions API (CAPI) telemetry.
4. **Qualification**: Dynamically evaluate against `Qualification.md` (0–100 score; Tier A/B/C).
5. **NEPQ Battlecard**: Generate 4-part cold call opener + 3-step objection handlers for Tier A/B leads.
6. **Compilation**: Save to `Clean_Enriched_Leads.csv` (`utf-8-sig`) and display summary in chat.

---

## 🎯 Verification Command
```powershell
python -m pytest tests/test_pipeline.py -v
```
