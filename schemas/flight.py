from pydantic import BaseModel
from typing import List, Dict

class FlightSearchRequest(BaseModel):
    origin: str
    destination: str

class FlightSearchResponse(BaseModel):
    flights: List[Dict[str, str]]