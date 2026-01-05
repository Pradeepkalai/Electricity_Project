from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import datetime

app = FastAPI()

# Enable CORS so the Frontend can talk to the Backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/predict")
async def get_prediction():
    # Example logic: Creating a 24-hour forecast
    now = datetime.datetime.now()
    labels = [(now + datetime.timedelta(hours=i)).strftime("%H:00") for i in range(24)]

    # This is where your Prophet/ARIMA model would output values
    # For now, we simulate a daily demand curve (lower at night, higher at day)
    values = [300 + (100 * (i / 12 if i <= 12 else (24 - i) / 12)) for i in range(24)]

    return {
        "labels": labels,
        "values": values,
        "unit": "MW"
    }


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)