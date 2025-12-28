from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime

app = FastAPI(
    title="LLM Incident Guardian",
    description="Production-grade observability demo for LLMs",
    version="0.1.0"
)

# ---------
# Models
# ---------

class GenerateRequest(BaseModel):
    prompt: str

class GenerateResponse(BaseModel):
    response: str
    timestamp: str


# ---------
# Routes
# ---------

@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "service": "llm-incident-guardian",
        "time": datetime.utcnow().isoformat()
    }


@app.post("/generate", response_model=GenerateResponse)
def generate_text(payload: GenerateRequest):
    """
    Dummy LLM endpoint 
    """
    dummy_response = f"Echo: {payload.prompt}"

    return {
        "response": dummy_response,
        "timestamp": datetime.utcnow().isoformat()
    }
