from fastapi import FastAPI
from .ai_engine import ai_engine
from pydantic import BaseModel
from fastapi import HTTPException, Request
import time


class PromptSchema(BaseModel):
    text: str

app = FastAPI(title="Hackathon AI Starter")

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.perf_counter()

    response = await call_next(request)

    process_time = time.perf_counter() - start_time

    response.headers['X-Process-Time'] = f"{process_time:.4f}s"
    print(f"Path: {request.url.path} | Duration: {process_time:.4f}s")

    return response

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