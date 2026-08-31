# 🎯 Lead Qualification & Enrichment Multi-Agent System

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-emerald.svg)](LICENSE)
[![MCP Enabled](https://img.shields.io/badge/MCP-Enabled-purple.svg)](https://modelcontextprotocol.io)
[![Ruflo Supported](https://img.shields.io/badge/Ruflo-Agency_Agents-indigo.svg)](https://github.com/msitarzewski/agency-agents)
[![Security: 0/100 Low Risk](https://img.shields.io/badge/SkillSpector-0%2F100_Passed-brightgreen.svg)](#security-audit)

> An autonomous, sharded multi-agent lead enrichment pipeline. Ingests raw Meta Ads Library CSV exports, deduplicates advertiser entities, partitions workload across concurrent Manager Pods (`asyncio.Semaphore(4)`), executes parallel deep research and headless browser audits via MCP tools, dynamically qualifies leads against user-defined `Qualification.md` rules, and synthesizes 4-part **Jeremy Miner NEPQ** cold call battlecards into an Excel-ready CSV.

---

## 🗺️ System Architecture

![Lead Enrichment Multi-Agent System](lead_enrichment_multi_agent_system.png)

---

## ⚡ Key Capabilities

- **👑 High-Level CEO Deduplication Engine**: Clusters multi-row raw Meta Ads CSV exports by Page ID and domain into canonical `Common_Info` and `Ads[]` JSON entities.
- **⚡ Dynamic Shard Allocation**: Automatically calculates the required concurrency budget and partitions leads across isolated Manager Pods.
- **🛡️ Concurrency Throttling & Fault Isolation**: Enforces `asyncio.Semaphore(4)` per pod to prevent rate-limit blocks and Playwright crashes. Failing client URLs are sandboxed without dropping successful records.
- **🟢 Stream 1 (Deep Research & Revenue)**: Analyzes creative angles, ad copy hooks, monthly spend brackets ($), and models wasted ad spend leakage ($/mo).
- **🟣 Stream 2 (Vision & Headless Browser Audit)**: Audits Mobile Largest Contentful Paint (LCP), Core Web Vitals, Meta Pixel & Conversions API (CAPI) server telemetry, and multi-touchpoint social channels.
- **♟️ Stage 3 (Dynamic Qualification Engine)**: Dynamically evaluates leads against custom criteria in [`Qualification.md`](Qualification.md) to generate composite 0–100 scores and assign Tiers (Tier A: Hot, Tier B: Warm, Tier C: Unqualified).
- **🎯 Stage 4 (Jeremy Miner NEPQ Behavioral Persuasion)**: Generates 4-part cold call scripts (Pattern Interrupt $\rightarrow$ Situation $\rightarrow$ Problem Awareness $\rightarrow$ Non-Pushy Pitch) and 3-step objection handlers (*In-House Agency, Budget/Price, Send Email*).
- **📊 Compilation & Multi-Channel Dispatch**: Exports ranked leads to `Clean_Enriched_Leads.csv` (`utf-8-sig` BOM) and dispatches alerts via SMTP Morning Email and Discord/Slack Webhooks.

---

## 🚀 Quick Start

### 1. Installation
```powershell
git clone https://github.com/DivyanshuAadi/lead-enrichment-multi-agent-system.git
cd lead-enrichment-multi-agent-system
pip install -r requirements.txt
```

### 2. Run the Autonomous Pipeline (CLI)
```powershell
python run_pipeline.py
```

### 3. Run Test Suite
```powershell
python -m pytest tests/test_pipeline.py -v
```

---

## 🤖 Cross-Agent Usage (Zero-Script Prompt Execution)

You can install and use this system directly across any AI coding agent:

### In Antigravity (Google Deepmind)
1. Open this directory as your active workspace.
2. Drop your raw Meta Ads CSV into chat and prompt:
   > *"Enrich my raw Meta ads CSV with Qualification.md using the multi-agent pipeline."*

### In Claude Code (With Ruflo Plugin)
1. Launch Claude Code in the repository folder:
   ```powershell
   claude
   ```
2. Prompt:
   > *"Process sample_meta_ads.csv using Qualification.md with the agency-agents topology."*

### In Claude Code (Vanilla / Without Ruflo)
```text
Execute the lead qualification and NEPQ enrichment pipeline on sample_meta_ads.csv following CLAUDE.md.
```

### In GitHub Copilot / Codex / DeepSeek Harness / Cursor / Cline
- Agents automatically detect [`AGENTS.md`](AGENTS.md) and [`plugin.json`](plugin.json).
- Prompt:
   > *"Analyze sample_meta_ads.csv using the multi-agent architecture in AGENTS.md, qualify against Qualification.md, and export Clean_Enriched_Leads.csv."*

---

## 🔌 Dynamic MCP Tool Integration

This repository includes standardized Model Context Protocol (MCP) bindings in [`.mcp.json`](.mcp.json):

| MCP Server | Tools Active | Purpose |
|---|---|---|
| **`facebook-ads-library`** | `search_facebook_ads`, `analyze_ad_creative_elements` | Live Meta campaign verification & ad spend telemetry |
| **`agent-reach`** | `get_status`, `verify_reachability` | Social channel footprint (Instagram, Facebook, WhatsApp) |
| **`playwright-browser`** | `navigate`, `screenshot`, `evaluate_script` | Headless Core Web Vitals (LCP) & Meta CAPI tag auditing |

*Note: The built-in [`tools/mcp_bridge.py`](tools/mcp_bridge.py) includes automatic fallback to high-performance local heuristics when MCP servers are offline.*

---

## 📁 Repository Structure

```
├── .agents/skills/lead-enrichment-agent/SKILL.md  # Antigravity native skill
├── .ruflo/ruflo.json                              # Ruflo agency agents configuration
├── agents/                                        # Multi-Agent Subsystems
│   ├── supervisor.py                              # Manager Pod Supervisor (Semaphore: 4)
│   ├── deep_research.py                           # Stream 1: Creative & Revenue Intel
│   ├── vision_browser.py                          # Stream 2: Vision & Playwright Audits
│   ├── qualification.py                           # Stage 3: Algorithmic Qualification
│   ├── qualification_parser.py                    # Dynamic Qualification.md Parser
│   └── nepq_sales_hook.py                         # Stage 4: Jeremy Miner NEPQ Engine
├── tests/
│   └── test_pipeline.py                           # Pytest unit & integration test suite
├── tools/
│   └── mcp_bridge.py                              # Dynamic MCP tool adapter
├── .mcp.json                                      # MCP server configurations
├── AGENTS.md                                      # Universal agent hierarchy specification
├── CLAUDE.md                                      # Claude Code orchestration instructions
├── HOW_TO_USE.md                                  # Complete user & model routing guide
├── Lead_Enrichment_Multi_Agent_System.md          # Master technical architecture document
├── lead_enrichment_multi_agent_system.excalidraw  # Native Excalidraw diagram
├── lead_enrichment_multi_agent_system.png         # Rendered high-res diagram
├── models.py                                      # Pydantic / Dataclass schemas
├── models_config.json                             # Configurable model routing matrix
├── deduplicator.py                                # CEO Meta Ads CSV deduplication engine
├── dynamic_code_generator.py                      # Dynamic schema code synthesizer
├── ceo_orchestrator.py                            # CEO Orchestration & dynamic sharder
├── postprocessor.py                               # DataFrame compiler & CSV exporter
├── notifier.py                                    # Multi-channel SMTP & Webhook alerts
├── Qualification.md                               # User qualification & outreach criteria
├── run_pipeline.py                                # CLI pipeline runner
├── sample_meta_ads.csv                            # Sample Meta Ads Library dataset
├── plugin.json                                    # Universal Plugin Manifest
├── install_plugin.ps1                             # 1-Click portable installer script
├── requirements.txt                               # Python dependencies
├── LICENSE                                        # MIT License
└── README.md                                      # Project documentation
```

---

## 🛡️ Security Audit

This repository has been audited with NVIDIA's **SkillSpector** security engine:
- **Risk Assessment Score**: `0/100 (LOW)`
- **Vulnerabilities Detected**: `0`
- **Execution Scripts**: Safe, clean, and isolated.

---

## 📄 License

Distributed under the MIT License. See [`LICENSE`](LICENSE) for details.
