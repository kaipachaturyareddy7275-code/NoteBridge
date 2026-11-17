from fastapi import FastAPI

app = FastAPI(title="NoteBridge")

@app.get("/")
def home():
    return {"message": "Welcome to NoteBridge!"}