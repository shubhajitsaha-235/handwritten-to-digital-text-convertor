from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import numpy as np
import cv2
from PIL import Image
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 👉 Point this to where Tesseract is installed on your PC
# Example for Windows:
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def preprocess_image(image_bytes):
    img = Image.open(io.BytesIO(image_bytes)).convert("L")  # grayscale
    img = np.array(img)

    # Resize (helps Tesseract if handwriting is small)
    h, w = img.shape
    if w < 1000:
        scale = 2
        img = cv2.resize(img, (w*scale, h*scale), interpolation=cv2.INTER_CUBIC)

    # Denoise
    img = cv2.medianBlur(img, 3)

    # Threshold (binarize)
    img = cv2.adaptiveThreshold(
        img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY, 35, 11
    )

    return img


@app.post("/ocr/")
async def ocr(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        img = preprocess_image(image_bytes)

        # OCR with Tesseract
        text = pytesseract.image_to_string(img, lang="eng")

        if not text.strip():
            return {"text": "⚠️ No text detected."}

        return {"text": text.strip()}

    except Exception as e:
        print("❌ OCR Error:", e)
        return {"error": str(e)}
