from fastapi import APIRouter

from database import ParafieDB
from models import Parafia

router = APIRouter()

@router.get("/get", response_model=list[Parafia])
async def get():
    return ParafieDB().get_all()

@router.post("/insert")
async def add(parafia: Parafia):
    ParafieDB().add(parafia.nazwa)

@router.post("/remove")
async def remove(id: int):
    ParafieDB().remove(id)