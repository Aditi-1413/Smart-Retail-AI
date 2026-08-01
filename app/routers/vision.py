import os
import shutil

from fastapi import APIRouter, UploadFile, File

from app.services.product_service import predict_product
from app.services.face_service import recognize_face

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@router.post("/predict-product")
async def predict_product_api(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return predict_product(file_path)


@router.post("/recognize-face")
async def recognize_face_api(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    return recognize_face(file_path)