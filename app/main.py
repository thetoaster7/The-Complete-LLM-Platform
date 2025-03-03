from fastapi import FastAPI
from app.routers.user_router import router as user_router
from app.database import Base,engine
import app.models

app=FastAPI(title="Generative AI Platform Backend")

app.include_router(user_router,prefix="/users",tags=["Users"])
#app.include_router(audio_router.router,prefix="/audio",tags=["Audio"])

@app.on_event("startup")
def startup():
    print("Creating table if not exist")
    Base.metadata.create_all(bind=engine)
@app.get("/")
def home():
    return {"message": "Welcome to the complete LLM Platform"}
