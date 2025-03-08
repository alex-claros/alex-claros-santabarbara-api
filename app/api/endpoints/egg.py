from fastapi import APIRouter, File, UploadFile, HTTPException
from domain.use_cases.detect_egg_viability import detect_egg_viability
from fastapi.responses import JSONResponse
import shutil
import os

router = APIRouter(
    prefix="/eggs",
    tags=["Huevos"]
)

@router.post("/detect")
async def detect_egg(file: UploadFile = File(...)):
    # Guardar el archivo subido temporalmente
    temp_file_path = f"temp_{file.filename}"
    with open(temp_file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    try:
        result = detect_egg_viability(temp_file_path)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(temp_file_path)

    return JSONResponse(content=result)
