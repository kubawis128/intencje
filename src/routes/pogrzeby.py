from fastapi import APIRouter
from fastapi.responses import FileResponse

from database import PogrzebyDB, IntencjeDB, ParafieDB
from models import Pogrzeb, Intencja

import pdfkit
import base64 

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

@router.get("/download", response_class=FileResponse)
async def download(show: bool, id: int):
    
    with open('topdftemplate.html', 'r') as file: 
        data = file.read()
    pogrzeb = PogrzebyDB().getById(id)
    tmer = f"""
        
            <p>Intencje zamówoione dla {pogrzeb.imie} {pogrzeb.nazwisko} {"na mszę dnia: " + pogrzeb.date_mszy.strftime('%d-%m-%Y %H:%M') if pogrzeb.date_mszy != None else ""}</p>
            <p>Pogrzeb w dniu: {pogrzeb.date.strftime('%d-%m-%Y')}</p>
        
            """
    data = data.replace("%wstep%", tmer)
    
    tmp = ""
    for intencja in IntencjeDB().get_for(pogrzeb.id):
        if show:
            tmp += f"""
                        <p>Intencja od {intencja.od_kogo} za {int(intencja.kwota)} zł</p>
                    """
        else:
            tmp += f"""
                        <p>Intencja od {intencja.od_kogo}</p>
                    """
    data = data.replace("%table%", tmp)

    tmp_pdf = pdfkit.from_string(data, False)
    with open('tmp.base64', "wb") as f:
        f.write(base64.b64encode(tmp_pdf))
    
    return "tmp.base64"
