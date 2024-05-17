#!/usr/bin/python
from fastapi import FastAPI
from api.v1.views import router, about_router



app = FastAPI()
app.include_router(router)
app.include_router(about_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
