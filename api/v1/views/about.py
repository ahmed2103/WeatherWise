#!/usr/bin/python3
from . import about_router
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
@about_router.get("/")
async def about(request: Request):
    """About page."""
    return templates.TemplateResponse("about.html", {"request": request})