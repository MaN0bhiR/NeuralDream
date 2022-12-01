from fastapi import FastAPI , File 
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse , StreamingResponse ,  Response 
import PIL.Image as Image 
import io
import os
import ArtMaker


app = FastAPI()

origins = ["http://localhost:3000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def image_to_byte_array(image: Image) -> bytes:
  
  return image.tobytes()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/uploadContent")
async def receiveImage(file: bytes = File(...)):
    image = Image.open(io.BytesIO(file))
    if os.path.isfile('tempCont.jpg'):
        os.remove('tempCont.jpg')
    image.save('tempCont.jpg')

    return int(1)

@app.post("/uploadStyle")
async def receiveImage(file: bytes = File(...)):
    image = Image.open(io.BytesIO(file))
    if os.path.isfile('tempSty.jpg'):
        os.remove('tempSty.jpg')
    image.save('tempSty.jpg')

    return int(1)

@app.get("/startTraining")
def start_training():
    headers = {'Content-Disposition': 'inline; filename="image.png"'}
    if os.path.isfile('tempSty.jpg') and os.path.isfile('tempCont.jpg'):
        image_Generator = ArtMaker.start_training('tempCont.jpg','tempSty.jpg')
        
        return StreamingResponse(content=image_Generator,headers=headers, media_type="image/png")
    
    else:
        return "Something Went Wrong. Please Try again"
