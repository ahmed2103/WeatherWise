#!/usr/bin/python3
"""Module for forecast view"""
from requests import get
from api.v1.views import router
from typing import Optional
from models import storage
from datetime import datetime, timedelta
from models.user import User
from models.location import Location
from fastapi import Request, Response

url = 'https://api.openweathermap.org/data/2.5/forecast/'
api_key = 'bacd9cc5a7f5a2ac5b557498678ed9d0'


@router.get('/forecast')
def forecast(request: Request, response: Response,
             city: str, country_code: Optional[str] = None,
             time_type: Optional[str] = 'daily',
             limit: Optional[str] = '7'):
    """Get forecast data"""
    units = 'C'
    token = request.cookies.get('token')
    if token:
        user = storage.get(User, token)
        try:
            units = user.prefered_units
        except AttributeError:
            token = None
        params = {'q': city.capitalize() if country_code is None
    else city.capitalize()+',' + country_code,
                'units': 'imperial' if units == 'F' else 'metric',
                  'cnt': limit,
              'appid': api_key}
    final_url = url + time_type
    try:
        responser = get(url, params=params)
    except Exception as e:
        return {'error': e}
    if responser.status_code == 404:
        return {'error': 'City not found'}
    if responser.status_code == 401:
        return {'error': 'Invalid 3rd party API key'}
    try:
        responserj = responser.json()
    except Exception as e:
        return {'error': '3rd party rseponse cannot be converted to JSON'}
    if token is None:
        user = User()
        storage.new(user)
        storage.save()
        token = user.id
        response.set_cookie(key='token', value=token,
                            max_age=31536000, expires=timedelta(seconds=31536000))
        cities = []
    else:
        user.last_active = datetime.now()
        cities = [x[0] for x in storage.user_locations(user.id)]
    if cities is None or city not in cities:
        location = Location(user_id=user.id, city_name=city.capitalize(),
                            country_code=responserj.get('city').get('country'),
                            latitude=responserj.get('city').get('coord').get('lat'),
                            longitude=responserj.get('city').get('coord').get('lon'))
        storage.new(location)
        storage.save()
    return responserj