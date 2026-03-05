from pydantic import BaseModel
from typing import List, Optional
import datetime
class MetricData(BaseModel):
    signup_conversion: float
    conversion_dropoff: str
    page: str
    previous_week_rate: float
    delta: float
class Hypothesis(BaseModel):
    id: str = ""
    rank: int
    hypothesis: str
    rationale: str
    predicted_lift_pct: float
    test_element: str
class Variant(BaseModel):
    experiment_id: str
    control_text: str
    variant_a_text: str
    variant_b_text: str
class Experiment(BaseModel):
    id: str = ""
    hypothesis: str
    status: str = "running"
    created_at: datetime.datetime = datetime.datetime.now()
    results: Optional[dict] = None
class Learning(BaseModel):
    id: str = ""
    document: str
    metadata: dict
class AgentStatus(BaseModel):
    last_run: Optional[str] = None
    status: str = "idle"
