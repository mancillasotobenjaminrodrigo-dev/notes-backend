from fastapi import APIRouter, HTTPException
from app.schemas.note import Note, CreatedNote, UpdateNote
from app.clients.firestore import get_firestore_client
from typing import Dict, List
from google.cloud import firestore


router = APIRouter(prefix="/notes", tags=["notes"])


@router.get("", status_code=200)
async def get_notes() -> Dict[str, List[Note]]:
    db = get_firestore_client()
    collection_ref = db.collection("notes").order_by("updated_at", direction=firestore.Query.DESCENDING)

    notes = []

    docs = collection_ref.stream()
    for doc in docs:
        note_data = doc.to_dict()
        note_data["created_at"] = note_data["created_at"].isoformat()
        note_data["updated_at"] = note_data["updated_at"].isoformat()
        notes.append(note_data)

    return {"notes": notes}

@router.post("", status_code=201)
async def create_note(note_data: CreatedNote) -> Dict[str, Note]:
    db = get_firestore_client()
    collection_ref = db.collection("notes")

    doc_ref = collection_ref.document()
    now = firestore.SERVER_TIMESTAMP

    new_note = {
        "id": doc_ref.id,
        "title": note_data.title,
        "content": note_data.content,
        "created_at": now,
        "updated_at": now
    }

    doc_ref.set(new_note)

    doc = doc_ref.get()
    note_stored = doc.to_dict()

    return {
        "note":{
            "id": note_stored["id"],
            "title": note_stored["title"],
            "content": note_stored["content"],
            "created_at" : note_stored["created_at"].isoformat(),
            "updated_at": note_stored["updated_at"].isoformat(),     
    }
    }

@router.get("/{note_id}", status_code=200)
async def get_note_by_id(note_id: str) -> Dict[str, Note]:
    db = get_firestore_client
    collection_ref = db.collection("notes")

    doc_ref = collection_ref.document(note_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code=404, detail="Note not found")
    
    note_data = doc.to_dict()

    return {
        "note": {
            "id": note_data["id"],
            "title": note_data["title"],
            "content": note_data["content"],
            "created_at" : note_data["created_at"].isoformat(),
            "updated_at": note_data["updated_at"].isoformat(),    
        }

    }

@router.patch("/{note_id}", status_code=200)
async def update_note(note_id: str, note_data: UpdateNote) -> Dict[str, Note]:
    db = get_firestore_client()
    collection_ref = db.collection("notes")

    doc_ref = collection_ref.document(note_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code = 404, detail="Note not found")
    
    update_data = {}

    if note_data.title is not None:
        update_data["title"] = note_data.title
    if note_data.content is not None:
        update_data["content"] = note_data.content

    update_data["updated_at"] = firestore.SERVER_TIMESTAMP

    doc_ref.update(update_data) 

    updated_doc = doc_ref.get()
    updated_note = updated_doc.to_dict()

    return {
        "note": {
            "id": updated_note["id"],
            "title": updated_note["title"],
            "content": updated_note["content"],
            "created_at" : updated_note["created_at"].isoformat(),
            "updated_at": updated_note["updated_at"].isoformat(),    
        }

    }

@router.delete("/{note_id}", status_code=200)
async def selete_note(note_id: str) -> Dict[str, str]:
    db = get_firestore_client()
    colelction_ref = db.collection("notes")

    doc_ref = colelction_ref.document(note_id)
    doc = doc_ref.get()

    if not doc.exists:
        raise HTTPException(status_code = 404, detail="Note not found")
    
    doc_ref.delete()

    return{
        "message": f"Note with ID {note_id} deleted"
    }


