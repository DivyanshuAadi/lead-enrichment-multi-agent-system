# 📖 How to Use the Lead Enrichment Multi-Agent System

This system is completely **autonomous, schema-agnostic, and model-tiered**. You never need to write or run static code manually.

---

## 🏎️ 1. The 30-Second Quickstart (Zero-Script AI Execution)

You only need **2 files**:
1. **Your Raw Ad CSV** (e.g. `RAW.csv` from Meta Ads Library, Google Ads, or any CRM export).
2. **Your Qualification Directives** ([`Qualification.md`](Qualification.md)).

### Step 1: Open Your Coding Agent
Open this workspace in **Antigravity, Claude Code, GitHub Copilot, Codex, DeepSeek Harness, Cursor, or Cline**.

### Step 2: Give the Agent Your Files
Simply prompt:
> *"Here is `RAW.csv` and `Qualification.md`. Run the lead qualification and enrichment multi-agent pipeline."*

### Step 3: What the Agent Does Automatically
1. **⚡ Dynamic Code Generation**: The CEO agent inspects your CSV schema (whatever the column names are) and writes a custom deduplication parser on the fly.
2. **📦 Sharded Manager Pods**: Spawns isolated worker pods with `asyncio.Semaphore(4)` concurrency throttling.
3. **🟢 Stream 1 (Research)**: Uses lightweight models (`haiku` / `flash` / `mini`) to deconstruct hooks, ad copy, and calculate wasted ad leakage ($/mo).
4. **🟣 Stream 2 (Vision & Browser)**: Audits Core Web Vitals (Mobile LCP speed), Meta Pixel, and CAPI telemetry via MCP tools (`playwright`, `facebook-ads-library`, `agent-reach`).
5. **♟️ Stage 3 (Qualification)**: Dynamically applies your custom criteria from `Qualification.md` to score leads 0–100 and assign Tier A (Hot), Tier B (Warm), or Tier C.
6. **🎯 Stage 4 (Jeremy Miner NEPQ Engine)**: Uses flagship reasoning (`sonnet` / `gpt-4o`) to generate 4-part cold call scripts and 3-step objection handlers.
7. **📊 Instant Export**: Saves sorted results to [`Clean_Enriched_Leads.csv`](Clean_Enriched_Leads.csv) (`utf-8-sig` Excel BOM).

---

## ⚙️ 2. How to Select & Control AI Models (`models_config.json`)

To change which models run which agent, open [`models_config.json`](models_config.json):

```json
{
  "active_preset": "balanced",
  "presets": {
    "balanced": {
      "ceo_orchestrator": "claude-3-7-sonnet-20250219",
      "dynamic_code_generator": "claude-3-7-sonnet-20250219",
      "stream1_creative_research_subagent": "claude-3-5-haiku-20241022",
      "stream2_vision_browser_subagent": "claude-3-5-haiku-20241022",
      "stage3_qualification_subagent": "claude-3-5-haiku-20241022",
      "stage4_nepq_sales_hook_subagent": "claude-3-7-sonnet-20250219"
    }
  }
}
```

### Pre-Configured Presets:
- **`balanced`** *(Recommended)*: Flagship for CEO/Coder/NEPQ + Ultra-fast Haiku for research/vision/qualification subagents.
- **`max_cost_savings`**: 100% Claude 3.5 Haiku across all stages (fastest & cheapest).
- **`openai_preset`**: GPT-4o for CEO/NEPQ + GPT-4o-mini for subagents.
- **`deepseek_preset`**: DeepSeek-R1/V3 models.
- **`antigravity_preset`**: `inherit` for CEO + `flash` / `flash_lite` for subagents.

---

## 🤖 3. Platform-Specific Guides

### Option A: In Claude Code (With Ruflo Agency Agents)
1. In terminal: `claude`
2. Prompt:
   ```text
   Process RAW.csv using Qualification.md and models_config.json with Ruflo Agency Agents topology.
   ```

### Option B: In Claude Code (Without Ruflo / Vanilla)
1. In terminal: `claude`
2. Prompt:
   ```text
   Execute the lead enrichment workflow for RAW.csv following Qualification.md and CLAUDE.md.
   ```

### Option C: In Antigravity (Google Deepmind)
1. Open folder in Antigravity.
2. Drop `RAW.csv` and `Qualification.md` in chat.
3. Prompt:
   ```text
   Enrich RAW.csv using Qualification.md. Use flash subagents for research and vision audits.
   ```

### Option D: In GitHub Copilot / Cursor / DeepSeek Harness
1. Reference `@agent /enrich RAW.csv with Qualification.md`.
2. The agent reads `AGENTS.md` and executes the dynamic pipeline.

---

## 🛠️ 4. How to Customize Qualification Criteria

Edit [`Qualification.md`](Qualification.md) at any time:
- Change minimum spend threshold: `Minimum Estimated Ad Spend: $5,000/month`
- Change target industries: `Priority Niches: High-Ticket MedSpa, Solar, Roofing`
- Adjust mobile speed limits: `Mobile LCP > 3.0 seconds`
- Custom NEPQ directives or objection rebuttals.

The dynamic parser automatically extracts these rules and applies them on your next run!
