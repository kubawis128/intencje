from fastapi import APIRouter
from .parafie import router as parafie
from .pogrzeby import router as pogrzeby
from .intencje import router as intencje
router = APIRouter()

router.include_router(parafie, prefix="/parafie")
router.include_router(pogrzeby, prefix="/pogrzeby")
router.include_router(intencje, prefix="/intencje")