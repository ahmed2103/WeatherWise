#!/usr/bin/python3
"""Module for main page view"""
from api.v1.views import main_router
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory="templates")

@main_router.get("/")
async def main(request: Request):
    """Main page"""
    return templates.TemplateResponse("index.html", {"request": request})