from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"status": "ok", "app": "demo-app", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "ok"}
