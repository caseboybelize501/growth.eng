# Autonomous Growth Engine (growth.eng)

## Overview
The AI that runs your entire go-to-market loop without a growth team. In 2026, this entire loop can be closed by an agent.

## Architecture
Multi-agent pipeline with persistent memory:
┌─────────────────────────────────────────────────────┐
│                  AGENT ORCHESTRATOR                  │
│   Cron → ObserveAgent → HypothesisAgent →           │
│          CopywriterAgent → DeployAgent →             │
│          MonitorAgent → EvaluatorAgent →             │
│          MemoryAgent (stores learnings)              │
└─────────────────────────────────────────────────────┘

## Features
- Autonomous A/B testing loop
- Multi-agent system with persistent memory
- Integration with PostHog, CMS, and email providers
- Statistical significance analysis
- Real-time dashboard for monitoring agent activity

## Stack
- Frontend: Next.js (read-only agent activity dashboard)
- Orchestrator: Python (FastAPI + APScheduler)
- Agents: Python classes with observe(), reason(), act(), evaluate()
- Memory: ChromaDB (vector store for experiment learnings)
- Database: PostgreSQL (experiments, variants, results)
- Queue: Redis + RQ (inter-agent messaging)

## Endpoints
GET  /api/agent/status          → current agent pipeline state
GET  /api/experiments           → all experiments + results
GET  /api/learnings             → ChromaDB memory dump
POST /api/agent/trigger         → manual trigger (bypass cron)
POST /api/config                → set PostHog key, CMS credentials, ICP
GET  /health                    → { status, last_run, next_run }
