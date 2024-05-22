#!/usr/bin/python3
from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["api"],
)
about_router = APIRouter(
    prefix="/about",
    tags=["about"],
)
main_router = APIRouter(
    prefix="/",
    tags=["main"],
)
from api.v1.views.about import *
from api.v1.views.weather import *
from api.v1.views.forecast import *
from api.v1.views.locations import *
from api.v1.views.prefered_units import *
from api.v1.views.main import *