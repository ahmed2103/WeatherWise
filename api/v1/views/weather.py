#!/usr/bin/python3
"""Module for weather view"""
from requests import get
from api.v1.views import router
from typing import Optional


url = 'https://api.openweathermap.org/data/2.5/weather'
api_key = 'bacd9cc5a7f5a2ac5b557498678ed9d0'

@router.get('/weather')
def weather(city: str, country_code: Optional[str] = None, units: Optional[str] = 'C'):
    """Get weather data"""
    params = {'q': city if country_code is None else city+',' + country_code,
                'units': 'imperial' if units == 'F' else 'metric',
              'appid': api_key}
    response = get(url, params=params)
    return response.json()


