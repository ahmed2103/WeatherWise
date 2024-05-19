#!/usr/bin/python
"""module for the FastAPI app"""
from models import storage
from fastapi import FastAPI
from views import router, about_router


app = FastAPI()
app.include_router(router)
app.include_router(about_router)


@app.on_event("shutdown")
async def shutdown_event():
    """Shutdown event"""
    storage.close()


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
