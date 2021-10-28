from typing import Optional

import fastapi
from fastapi import Depends
from models.lcoation import Location
from services import openweather_service

router = fastapi.APIRouter()


@router.get('/api/weather/{city}')
def weather(loc: Location = Depends(), units: Optional[str] = 'metric'):
    result = openweather_service.get_report(loc.city, loc.state, loc.country, units)
    return result
