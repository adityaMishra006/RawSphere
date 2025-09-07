from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import traceback

# Use absolute imports (adjust based on your structure)
from AI.forecast_utils import forecast_monthly
from AI.surplus_utils import predict_surplus_from_forecast

app = FastAPI(title="Medicine Forecast API", version="1.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Backend is running 🚀", "status": "healthy"}

@app.get("/forecast_monthly")
def get_forecast():
    try:
        result = forecast_monthly()
        return result
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Forecast error: {str(e)}")

@app.get("/predict_surplus_auto")
def get_surplus_predictions():
    try:
        result = predict_surplus_from_forecast()
        return result
    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Surplus prediction error: {str(e)}")

# Add a health check endpoint
@app.get("/health")
def health_check():
    return {"status": "healthy", "endpoints": ["/", "/forecast_monthly", "/predict_surplus_auto"]}