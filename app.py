from fastapi import File, Form, UploadFile
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import io
from PIL import Image
import numpy as np
import uvicorn


app = FastAPI()

app.mount("/statics", StaticFiles(directory="statics"), name="static", )


templates = Jinja2Templates(directory="templates")

def slice_with_overlay(img, stride_x, stride_y, out):
   

    stride_x = out - stride_x
    stride_y = out - stride_y
    
    

    

    row = img.shape[0]
    col = img.shape[1]

    outer = (row // out) * out
    inner = (col // out) * out
    
    images = []

    for r in range(0, outer, stride_y):
        for c in range(0, inner + 1, stride_x):
            #satır boyutundan büyük çıkarsa satır boyutunu sınır alarak geriye out kadar geriden alır
            if r + out > row:

                #sütun boyutundan büyük çıkarsa sütun boyutunu sınır alarak geriye out kadar geriden alır
                if c + out > col:

                    # print(row - out, row, col - out, col)

                    images.append(img[row-out:row, col - out:col, :])
                    break
                    
                else:
                    #print(row - out, row, c, c + out)

                    # #etiketleri kayıtederken
                    images.append(img[row - out : row, c : c + out, :])

                 
            elif c + out > col:

                #print(r, r + out, col - out, col)
                images.append(img[r : r + out, col - out : col, :])
                break
            else:
                #print(r , r + out, c, c + out)

                images.append(img[r : r + out, c : c + out, :])

    return images

@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})

@app.post("/patch")
async def patch(request:Request, file_upload: UploadFile = File(...), stride_x: int = Form(...), stride_y: int = Form(...), out: int = Form(...)):
    file = await file_upload.read()
    bytes_io = io.BytesIO(file)
    img = Image.open(bytes_io)
    img = np.array(img)
    pathced_images = slice_with_overlay(img, stride_x=stride_x, stride_y=stride_y, out=out)
    
    image_paths = []
    for i in range(len(pathced_images)):
        img = Image.fromarray(pathced_images[i])
        img.save(f"statics/patched/{i}.png")
        image_paths.append(f"/statics/patched/{i}.png")
    
    return  templates.TemplateResponse("patch.html", {"request":request,"image_paths": image_paths})
    
    