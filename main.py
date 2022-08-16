from fastapi import FastAPI
from fastapi.responses import FileResponse
app = FastAPI()

@app.get("/")
def name():
    return 'hello2'

@app.get("/data")
def data():
    return  {'hello' : 12345 }

@app.get("/html")
def html():
    return  FileResponse('index.html')
from pydantic import BaseModel
class Model(BaseModel):
    name: str
    phone: int 


@app.post("/html")
def save(data : Model):
    print(date)
    return  'completed'

    
    