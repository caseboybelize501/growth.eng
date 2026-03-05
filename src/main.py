from fastapi import FastAPI, HTTPException
from apscheduler.schedulers.background import BackgroundScheduler
import asyncio
from src.orchestrator import GrowthOrchestrator
from src.models import AgentStatus
app = FastAPI(title="Autonomous Growth Engine")
orchestrator = GrowthOrchestrator()
scheduler = BackgroundScheduler()
scheduler.add_job(func=orchestrator.run_pipeline, trigger="interval", minutes=10)
scheduler.start()
@ app.get("/api/agent/status")
async def get_agent_status():
    return orchestrator.get_status()
@ app.get("/api/experiments")
async def get_experiments():
    return orchestrator.get_experiments()
@ app.get("/api/learnings")
async def get_learnings():
    return orchestrator.get_learnings()
@ app.post("/api/agent/trigger")
async def trigger_manual_run():
    try:
        asyncio.run(orchestrator.run_pipeline())
        return {"message": "Manual run triggered"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@ app.post("/api/config")
async def set_config(config: dict):
    orchestrator.set_config(config)
    return {"message": "Configuration updated"}
@ app.get("/health")
async def health_check():
    return {
        "status": "healthy",
        "last_run": orchestrator.last_run,
        "next_run": scheduler.get_jobs()[0].next_run_time if scheduler.get_jobs() else None
    }
