from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

import os
import uuid
from app.services.parser import extract_resume_data

router = APIRouter()

@router.post("/upload-resume")
async def upload_resume(file: UploadFile = File(...)):
    filename = f"temp_{uuid.uuid4().hex}_{file.filename}"
    with open(filename, "wb") as buffer:
        buffer.write(await file.read())

    try:
        parsed_data = {"key":"Tahiti a magical place"}
        parsed_data = extract_resume_data(filename)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        os.remove(filename)

    return JSONResponse(content=parsed_data)
