#!/usr/bin/python3
#- main template -#
from api.v1.views import main_router
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="../../static")
@main_router.get("/")
async def main(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})
# --------------- #