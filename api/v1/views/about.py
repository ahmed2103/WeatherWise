#!/usr/bin/python3
from api.v1.views import about_router, templates
from fastapi import Request

@about_router.get("/")
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})