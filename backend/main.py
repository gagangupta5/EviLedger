from fastapi import FastAPI

app = FastAPI(
    title="EviLedger API",
    description="Blockchain based digital Evidence Management System",
    version="1.0.0"
)
@app.get("/")
def home():
    return {
        "message": "EviLedger Backend is running"
    }