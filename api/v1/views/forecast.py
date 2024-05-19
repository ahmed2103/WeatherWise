#!/usr/bin/python3
"""Module for forecast view"""
from requests import get
from . import router
from typing import Optional
from models.user import User
from models.location import Location
from datetime import datetime, timedelta
from fastapi import Request, Response
from models import storage

request: Request
response: Response

url = 'https://api.openweathermap.org/data/2.5/forecast/'
api_key = 'bacd9cc5a7f5a2ac5b557498678ed9d0'


@router.get('/forecast')
async def forecast(city: str, country_code: Optional[str] = None,
             units: Optional[str] = 'C',
             time_type: Optional[str] = 'daily'):
    """Get forecast data"""
    params = {'q': city if country_code is None else city+',' + country_code,
                'units': 'imperial' if units == 'F' else 'metric',
              'appid': api_key}
    final_url = url + time_type
    response = get(url, params=params).json()
    token = request.cookies.get('token')
    if token is None:
        user = User()
        token = user.id
        response.set_cookie(key='token', value=token
                            , expires=datetime.now() + timedelta(days=36))
    else:
        user = storage.get(User, token)
    if response.status_code == 200:
        if city not in storage.user_locations(user.id):
            location = Location(user_id=user.id, city_name=city,
                            country_code=country_code,
                            latitude=response.get('coord').get('lat'),
                            longitude=response.get('coord').get('lon'))
            storage.new(location)
            storage.save()
    return response


