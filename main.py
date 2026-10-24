from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def anasayfa():
    return {"mesaj" : "Merhaba"}
@app.get("/selam")
def selam():
    return {"mesaj": "Selam"}