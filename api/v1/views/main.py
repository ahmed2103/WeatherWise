#!/usr/bin/python3
"""Module for main page view"""
from api.v1.views import main_router, templates
from fastapi import Request
from fastapi.templating import Jinja2Templates
from requests import get



@main_router.get("/")
async def main(request: Request):
    """Main page"""
    ip = request.headers.get('X-Forwarded-For')
    try:
        responser = get(f'https://freegeoip.app/json/{ip}').json()
    except Exception:
        try:
            responser = get(f'http://ip-api.com/json/{ip}').json()
        except Exception:
            responser = {'city': None, 'country_code': None}
    city = responser.get('city')
    country_code = responser.get('country_code')
    params = {'q': city + ',' + country_code,
              'appid': 'bacd9cc5a7f5a2ac5b557498678ed9d0',
                'units': 'metric'}
    try:
        responser_w = get('https://api.openweathermap.org/data/2.5/weather', params=params).json()
    except Exception:
        responser_w = {'main': {'temp': None}}
    return templates.TemplateResponse("index.html", {"request": request, "city": city, "country_code": country_code, "temp": responser_w.get('main').get('temp'),
                                                     "description": responser_w.get('weather')[0].get('description')})