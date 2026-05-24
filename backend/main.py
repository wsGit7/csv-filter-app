import csv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serwowanie statycznych plików (frontend)
app.mount("/static", StaticFiles(directory="static"), name="static")

# Strona główna
@app.get("/")
def root():
    return FileResponse("static/index.html")

# Endpoint filtrujący
@app.get("/filter")
def filter_data(brand: str = None, speed: int = None, number: int = None):
    results = []
    with open("data.csv", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        for row in reader:
            if brand and row["brand"] != brand:
                continue
            if speed and int(row["speed"]) != speed:
                continue
            if number and int(row["number"]) != number:
                continue
            results.append(row)
    return results
