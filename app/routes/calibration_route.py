from fastapi import APIRouter, UploadFile, File, HTTPException
from app.controllers.calibration_controller import CalibrationController
from fastapi.responses import JSONResponse

router = APIRouter(prefix="/calibration")
controller = CalibrationController()

@router.post("/process/")
async def process_calibration(
    file: UploadFile = File(...),
    expected_r: int = 255,
    expected_g: int = 255,
    expected_b: int = 255
):
    try:
        image_content = await file.read()
        expected_rgb = {"r": expected_r, "g": expected_g, "b": expected_b}
        result = controller.process_calibration(image_content, expected_rgb)
        return JSONResponse(content=result.to_dict(), status_code=200)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))