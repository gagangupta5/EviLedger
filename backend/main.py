from fastapi import FastAPI

app = FastAPI(
    title="EviLedger API",
    description="Blockchain-Based Digital Evidence Management System",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "project": "EviLedger",
        "message": "EviLedger Backend is running"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "service": "EviLedger Backend"
    }
