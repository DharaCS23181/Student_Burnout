from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from model import predict

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend assets
app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")

# Serve React UI
@app.get("/")
def serve_frontend():
    return FileResponse("static/index.html")

# Prediction API
@app.post("/predict")
def get_prediction(data: dict):
    result = predict(data)
    return {"prediction": int(result)}