from fastapi import FastAPI
from pydantic import BaseModel
class YeniGorev(BaseModel):
    baslik:str 
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


@app.post("/gorevler")
def gorev_ekle(yeni: YeniGorev):
    print(yeni)
    en_buyuk_id=0
    for g in gorevler:
        if g["id"] > en_buyuk_id:
            en_buyuk_id = g["id"]
    yeni_id = en_buyuk_id+1
    gorev={"id":yeni_id,"baslik":yeni.baslik,"tamam":False}
    gorevler.append(gorev)
    return gorev

@app.delete("/gorevler/{gorev_id}")
def gorev_sil(gorev_id: int):
    for gorev in gorevler:
        if gorev["id"]== gorev_id:
            gorevler.remove(gorev)
            return{"mesaj":"silindi"}
    return {"mesaj":"bulunamadı"}
                    
