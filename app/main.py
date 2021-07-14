from fastapi import Depends, FastAPI

from .routers import excel, csv

app = FastAPI(
    title="Join FastAPI and Pandas",
    description="This is a simple program to demonstrate how to use the FastAPI and Pandas together",
    version="1.0.0",
)

app.include_router(excel.router)
app.include_router(csv.router)
