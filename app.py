import pandas as pd
import joblib
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from pathlib import Path

app = FastAPI()

# Setup templates
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(BASE_DIR / "templates"))

# Load model
model = joblib.load(BASE_DIR / "model.joblib")

# Load data for dropdowns
train = pd.read_csv(BASE_DIR / "data/train.csv")
val = pd.read_csv(BASE_DIR / "data/val.csv")
X_data = pd.concat([train, val], axis=0).drop(columns="price")

# Prepare options for dropdowns
options = {
    "airline": sorted(X_data.airline.unique().tolist()),
    "source": sorted(X_data.source.unique().tolist()),
    "destination": sorted(X_data.destination.unique().tolist()),
    "additional_info": sorted(X_data.additional_info.unique().tolist())
}

@app.get("/")
@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request, "title": "Home"})

@app.get("/predict")
async def predict_page(request: Request):
    return templates.TemplateResponse("predict.html", {
        "request": request,
        "title": "Predict",
        "options": options
    })

@app.post("/predict")
async def predict(
    request: Request,
    airline: str = Form(...),
    date_of_journey: str = Form(...),
    source: str = Form(...),
    destination: str = Form(...),
    dep_time: str = Form(...),
    arrival_time: str = Form(...),
    duration: int = Form(...),
    total_stops: int = Form(...),
    additional_info: str = Form(...)
):
    try:
        # HTML5 time inputs return HH:MM, but model might expect HH:MM:SS
        dep_time_str = dep_time if len(dep_time) == 8 else f"{dep_time}:00"
        arrival_time_str = arrival_time if len(arrival_time) == 8 else f"{arrival_time}:00"
        
        x_new = pd.DataFrame(dict(
            airline=[airline],
            date_of_journey=[date_of_journey],
            source=[source],
            destination=[destination],
            dep_time=[dep_time_str],
            arrival_time=[arrival_time_str],
            duration=[duration],
            total_stops=[total_stops],
            additional_info=[additional_info]
        ))
        
        prediction = model.predict(x_new)[0]
        message = f"The predicted price is {prediction:,.0f} INR!"
        
    except Exception as e:
        message = f"Error: {str(e)}"

    return templates.TemplateResponse("predict.html", {
        "request": request,
        "title": "Predict",
        "options": options,
        "output": message,
        "form_data": {
            "airline": airline,
            "date_of_journey": date_of_journey,
            "source": source,
            "destination": destination,
            "dep_time": dep_time,
            "arrival_time": arrival_time,
            "duration": duration,
            "total_stops": total_stops,
            "additional_info": additional_info
        }
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
