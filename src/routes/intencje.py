from fastapi import APIRouter

from database import IntencjeDB
from models import Intencja

router = APIRouter()

@router.get("/get_for", response_model=list[Intencja])
async def get(id: int):
    return IntencjeDB().get_for(id)

@router.post("/insert")
async def add(intencja: Intencja):
    IntencjeDB().add(intencja)

@router.post("/remove")
async def remove(id: int):
    IntencjeDB().remove(id)