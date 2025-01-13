from fastapi import FastAPI, UploadFile, File
import easyocr
from PIL import Image
import io
from fastapi.responses import HTMLResponse 
from fastapi.templating import Jinja2Templates 
from fastapi.requests import Request

reader = easyocr.Reader(['en'])  

app = FastAPI()
 
templates = Jinja2Templates(directory="templates")

def extract_text_from_image(image_bytes):
    """  """
    image = Image.open(io.BytesIO(image_bytes))
    # Convert the image to a format EasyOCR can read
    img_byte_arr = io.BytesIO()
    image.save(img_byte_arr, format='PNG')
    img_byte_arr = img_byte_arr.getvalue()
    result = reader.readtext(img_byte_arr)
    # Extract and return the text
    extracted_text = " ".join([text[1] for text in result])
    return extracted_text


@app.get("/", response_class=HTMLResponse) 
async def main_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/ocr/")
async def perform_ocr(file: UploadFile = File(...)):
    image_bytes = await file.read()
    extracted_text = extract_text_from_image(image_bytes)
    return {"text": extracted_text}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=8000)
