#!/usr/bin/python3
from api.v1.views import about_router
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
@about_router.get("/")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})