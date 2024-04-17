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
async def download(show: bool):
    

    with open('topdftemplate.html', 'r') as file: 
        data = file.read()
    tmp = ""
    for pogrzeb in PogrzebyDB().get_all():
        tmp += f"""
                <tr>
                    <td>{pogrzeb.imie} {pogrzeb.nazwisko}</td>
                    <td>{pogrzeb.date.strftime('%d-%m-%Y')}</td>
                    <td>{pogrzeb.date_mszy.strftime('%d-%m-%Y %H:%M') if pogrzeb.date_mszy != None else "Brak"}</td>
                    <td>{pogrzeb.parafia_id}</td>
                </tr>
                <tr>
                    <td colspan="4">
                        <table>
                            <tr>
                                <th colspan="4">Intencje</th>
                            </tr>
                """
        for intencja in IntencjeDB().get_for(pogrzeb.id):
            if show:
                tmp += f"""
                                <tr>
                                    <td colspan="3">{intencja.od_kogo}</td>
                                    <td>{int(intencja.kwota)} zł</td>
                                </tr>
                        """
            else:
                tmp += f"""
                                <tr>
                                    <td colspan="4">{intencja.od_kogo}</td>
                                </tr>
                        """
        tmp += """
                        </table>
                    </td>
                </tr>
                """
    data = data.replace("%here%", tmp)

    tmp_pdf = pdfkit.from_string(data, False)
    with open('tmp.base64', "wb") as f:
        f.write(base64.b64encode(tmp_pdf))
    
    return "tmp.base64"
