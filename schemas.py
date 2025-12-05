from pydantic import BaseModel
from datetime import date, time

class FlightPredictionInput(BaseModel):
    airline: str
    date_of_journey: date
    source: str
    destination: str
    dep_time: time
    arrival_time: time
    duration: int
    total_stops: int
    additional_info: str
