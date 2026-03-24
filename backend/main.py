from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from model import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")
@app.get("/")
def home():
    return {"message": "API Running"}

@app.post("/predict")
def get_prediction(data: dict):
    result = predict(data)
    return {"prediction": int(result)}