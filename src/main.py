from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from routes import main

from services.auth import get_current_user
import services.auth as auth
app = FastAPI()

app.include_router(main.router, prefix="/api", dependencies=[Depends(get_current_user)])
app.include_router(auth.router)

app.mount("/", StaticFiles(directory="frontend/", html=True), name="frontend")