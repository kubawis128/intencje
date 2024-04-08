from datetime import datetime
from fastapi import APIRouter

from database import PogrzebyDB
from models import Pogrzeb

router = APIRouter()

@router.get("/get", response_model=list[Pogrzeb])
async def get():
    return PogrzebyDB().get_all()

@router.post("/insert")
async def add(pogrzeb: Pogrzeb):
    PogrzebyDB().add(pogrzeb)
    
@router.post("/update")
async def update(pogrzeb: Pogrzeb):
    PogrzebyDB().update(pogrzeb)
    
@router.post("/remove")
async def remove(id: int):
    PogrzebyDB().remove(id)