#!/usr/bin/python3
"""Module for main page view"""
from api.v1.views import main_router, templates
from fastapi import Request
from requests import get



@main_router.get("/")
async def main(request: Request):
    """Main page"""
    ip = ''
    #ip = request.headers.get('X-Forwarded-For')
    try:
        responser = get(f'https://freegeoip.app/json/{ip}').json()
    except Exception:
        try:
            responser = get(f'http://ip-api.com/json/{ip}').json()
        except Exception:
            responser = {'city': None, 'country_code': None}
    longi = responser.get('longitude')
    lati = responser.get('latitude')
    params = {'lat': lati, 'lon': longi,
              'appid': 'bacd9cc5a7f5a2ac5b557498678ed9d0',
                'units': 'metric'}
    try:
        responser_w = get('https://api.openweathermap.org/data/2.5/weather', params=params).json()
    except Exception:
        responser_w = {'main': {'temp': None}}
    return templates.TemplateResponse("index.html", {
        "request": request,
        "city": responser_w.get('name'),
        "country": responser.get('country_name'),
        "temp": responser_w.get('main').get('temp'),
        "description": responser_w.get('weather')[0].get('description'),
        'icon': responser_w['weather'][0]['icon'],
        'humidity': responser_w['main']['humidity'],
        'wind': {
            'speed': responser_w['wind']['speed'],
            'deg': responser_w['wind']['deg']
        },
        'timezone': responser_w['timezone']
    })