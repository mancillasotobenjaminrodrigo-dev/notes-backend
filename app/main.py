from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.notes.endpoints import router as notes_router

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(notes_router)

#Endpoint básico "Hello wold"
@app.get("/")
def hello_world():
    return {"message": "Yo soy Optimus Prime"}

