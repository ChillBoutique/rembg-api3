from fastapi import FastAPI, UploadFile, File
from rembg import remove
from fastapi.responses import Response

app = FastAPI()

@app.post("/remove-background/")
async def remove_bg(file: UploadFile = File(...)):
    input_data = await file.read()
    output_data = remove(input_data)
    return Response(content=output_data, media_type="image/png")
