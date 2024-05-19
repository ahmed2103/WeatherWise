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
from .about import *
from .weather import *
from .forecast import *