from fastapi import FastAPI
from .ai_engine import ai_engine
from pydantic import BaseModel
from fastapi import HTTPException


class PromptSchema(BaseModel):
    text: str

app = FastAPI(title="Hackathon AI Starter")

@app.get("/")
def read_root():
    return {"hello": "world"}

@app.post("/analyze")
async def analyze(payload: PromptSchema):
    try:
        response = await ai_engine.generate_solution(prompt=payload.text)
        return {"status": "success","data": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@app.get("/list_model")
def list_model():
    return ai_engine.list_models()