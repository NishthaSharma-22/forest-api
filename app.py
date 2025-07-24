from fastapi import FastAPI
from fastapi.responses import FileResponse
import random


app = FastAPI()

images = "images"

image_names = [f"image{i}.jpg" for i in range(1,6)]
@app.get("/")
async def home_root():
    return {"message": "success"}

@app.get("/random-image")

def get_random_image():
    chosen = random.choice(image_names)
    return FileResponse(f"{images}/{chosen}")