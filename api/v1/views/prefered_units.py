#!/usr/bin/python3
"""Module for prefered units"""
from api.v1.views import router
from models import storage
from fastapi import Request
from models.user import User


@router.put('/prefered_units')
async def prefered_units(request: Request, units: str):
    """Set prefered units"""
    token = request.cookies.get('token')
    user = storage.get(User, token)
    user.prefered_units = units
    storage.save()
    return {'prefered_units': units}