from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Topic(BaseModel):
    topic: str

@app.post("/start_debate")
async def start_debate(topic: Topic):
    # Logic to start the debate with the given topic
    return {"message": f"Debate started on topic: {topic.topic}"}

@app.post("/stop_debate")
async def stop_debate():
    # Logic to stop the debate
    return {"message": "Debate stopped."}
