from fastapi import FastAPI
# from .task_manager.api import router
from task_manager.api import router

app = FastAPI()
app.include_router(router)
