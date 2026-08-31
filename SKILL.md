---
name: lead-enrichment-plugin
description: Universal Lead Qualification & Enrichment Multi-Agent Plugin. Ingests raw Meta Ads Library CSV, deduplicates into canonical business entities, dynamically shards workload across Manager Pods with Semaphore(4) throttling, executes parallel research and headless vision/CAPI audits via MCP tools, qualifies leads against user-provided Qualification.md, and synthesizes 4-part Jeremy Miner NEPQ cold call battlecards into Clean_Enriched_Leads.csv.
allowed-tools:
  - run_command
  - view_file
  - write_to_file
  - search_web
  - call_mcp_tool
---

# Universal Lead Qualification & Enrichment Multi-Agent Plugin

## Overview
This portable plugin enables any AI coding agent (Antigravity, Claude Code with/without Ruflo, GitHub Copilot, Codex, DeepSeek Harness, Cursor, Windsurf, Cline) to operate as an autonomous Lead Qualification & Enrichment pipeline.

## How to Use
1. Give the agent your RAW Meta Ads CSV (e.g. `RAW.csv` or `sample_meta_ads.csv`) and your `Qualification.md` file.
2. Instruct the agent:
   "Run the lead enrichment pipeline on RAW.csv with Qualification.md"
3. The agent dynamically parses `Qualification.md`, runs the Manager Pods with `asyncio.Semaphore(4)`, connects to active MCP servers (Meta Ads Library, Agent Reach, Playwright), and exports `Clean_Enriched_Leads.csv` (`utf-8-sig`).
