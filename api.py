from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
    return {"message": "Hello, Replit!"}

@app.get("/agents/")
async def create_agent(agent: str):
    return {"message": agent}

