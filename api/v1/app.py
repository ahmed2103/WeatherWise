#!/usr/bin/python
#     fix for PYTHONPATH issue    #
import sys
from os import path as os_path
sys.path.append(
    os_path.join(
        os_path.dirname(__file__),
        '..', '..'
        )
    )
# ------------------------------- #
from fastapi import FastAPI
from api.v1.views import router, about_router

app = FastAPI()
#     fix for CORS issue    #
from fastapi.middleware.cors import CORSMiddleware
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
# ------------------------------- #

app.include_router(router)
app.include_router(about_router)

#- main router -#
from api.v1.views import main_router
app.include_router(main_router)
# ------------- #

#- static files -#
from fastapi.staticfiles import StaticFiles
app.mount("/js", StaticFiles(directory="../../static/js"), name="static js")
app.mount("/css", StaticFiles(directory="../../static/css"), name="static css")
app.mount("/assets", StaticFiles(directory="../../static/assets"), name="static assets")
# --------------- #

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
