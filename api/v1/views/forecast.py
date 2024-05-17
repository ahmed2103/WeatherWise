#!/usr/bin/python3
"""Module for forecast view"""
from requests import get
from api.v1.views import router
from typing import Optional


url = 'https://api.openweathermap.org/data/2.5/forecast/'
api_key = 'bacd9cc5a7f5a2ac5b557498678ed9d0'


@router.get('/forecast')
def forecast(city: str, country_code: Optional[str] = None,
             units: Optional[str] = 'C',
             time_type: Optional[str] = 'daily'):
    """Get forecast data"""
    params = {'q': city if country_code is None else city+',' + country_code,
                'units': 'imperial' if units == 'F' else 'metric',
              'appid': api_key}
    final_url = url + time_type
    response = get(url, params=params)
    return response.json()