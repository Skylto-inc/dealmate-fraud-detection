from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import uvicorn

app = FastAPI(title="Fraud Detection Service")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class TransactionData(BaseModel):
    user_id: str
    amount: float
    merchant: str

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "fraud-detection-service", "features": ["fraud_analysis", "risk_scoring"]}

@app.post("/fraud/analyze")
async def analyze_transaction(transaction: TransactionData):
    return {
        "is_fraud": False,
        "confidence": 0.95,
        "risk_score": 0.1,
        "reasons": [],
        "service": "fraud-detection-service"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=3011)
