from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.clients.firestore import get_firestore_client

app = FastAPI()

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
def hello_world():
    return {"message": "Yo soy Optimus Prime"}

@app.get("/notes")
async def get_notes():
    db = get_firestore_client()
    collection_ref = db.collection("test-notes")

    notes = []

    docs = collection_ref.stream()
    for doc in docs:
        note_data = doc.to_dict()
        notes.append(note_data)

    return {"notes": notes}