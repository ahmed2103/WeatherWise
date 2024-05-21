#!/usr/bin/python3
"""Module for locations view"""
from api.v1.views import router
from fastapi import Request
from models import storage


@router.get('/locations')
async def get_user_locations(request: Request):
    """Get all locations"od user"""
    user_id = request.cookies.get('token')
    if user_id:
        return {'Cities, Country_code ': sorted(storage.user_locations(user_id),
                                                key=lambda x: x[0])}
