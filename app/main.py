# app/main.py
from fastapi import FastAPI
from .routes import chat

app = FastAPI()

app.include_router(chat.router, tags=["chat"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
