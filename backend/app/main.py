from fastapi import FastAPI

app = FastAPI(
    title="MARIS API",
    description="AI study companion backend",
    version="0.1.0",
)

@app.get("/")
async def root():
    return {
        "name": "MARIS",
        "status": "running",
        "version": "0.1.0",
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
