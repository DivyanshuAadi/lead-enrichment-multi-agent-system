---
name: lead-enrichment-agent
description: Autonomous Meta Ads Lead Qualification & Enrichment Multi-Agent System. Ingests raw Facebook Meta Ads Library CSVs, clusters into deduplicated entities, shards across manager pods, audits web vitals and CAPI in parallel, qualifies leads against Qualification.md, synthesizes Jeremy Miner NEPQ outreach battlecards, and exports Clean_Enriched_Leads.csv.
allowed-tools:
  - run_command
  - view_file
  - write_to_file
  - search_web
  - call_mcp_tool
---

# Lead Enrichment & Qualification Agent Skill

Use this skill whenever the user provides, uploads, or references a raw Meta Ads Library CSV file.

## Execution Workflow

1. **Phase 1: Ingestion & Deduplication**:
   - Ingest the user-provided CSV.
   - Group rows by `page_id` into canonical JSON objects with `Common_Info_Found_Among_Ads` and `Ads` array.
2. **Phase 2: Shard Partitioning**:
   - Partition workload across Manager Pods with `asyncio.Semaphore(4)` concurrency lock.
3. **Phase 3: Multi-Agent Audit**:
   - **Stream 1**: Creative angles, estimated monthly spend ($), and wasted spend leakage ($/mo).
   - **Stream 2**: Headless landing page audit, Mobile LCP speed, Meta Pixel, and CAPI telemetry status.
   - **Qualification**: Evaluate against `Qualification.md` to compute a 0–100 score and assign Tier A, Tier B, or Tier C.
   - **NEPQ Synthesis**: For Tier A/B leads, construct the 4-part Jeremy Miner cold hook and 3-step objection handlers.
4. **Phase 4: Output Compilation**:
   - Save sorted results to `Clean_Enriched_Leads.csv` (`utf-8-sig`).
   - Render an executive briefing table directly in chat.
