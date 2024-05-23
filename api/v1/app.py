#!/usr/bin/python3

from models import storage
from fastapi import FastAPI
from api.v1.views import router, about_router, main_router


app = FastAPI()
app.include_router(router)
app.include_router(about_router)
app.include_router(main_router)

@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    storage.close()

@app.on_event("startup")
async def startup_event():
    """Startup event"""
    storage.reload()

if __name__ == "__main__":
    from uvicorn import run
    run(app, host="0.0.0.0", port=8000)
