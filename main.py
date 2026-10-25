from fastapi import FastAPI
app= FastAPI()
@app.get("/")
def anasayfa():
    return {"mesaj" : "Merhaba"}
@app.get("/selam")
def selam():
    return {"mesaj": "Selam"}
gorevler = [
    {"id":1, "baslik": "Python tekrar et", "tamam": False},
    {"id":2,"baslik":"FastAPI ogren","tamam":False},{"id":3,"baslik":"Yeni Gorev", "tamam":False}
]
@app.get("/gorevler")
def gorevleri_listele():
    return gorevler