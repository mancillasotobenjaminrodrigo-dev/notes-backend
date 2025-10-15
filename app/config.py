import os
from dotenv import load_dotenv

load_dotenv(".env.local")

class Settings:
    GCP_PROJECT_ID: str = os.getenv("GCP_PROJECT_ID")
    FIRESTORE_DATABASE_ID: str = os.getenv("FIRESTORE_DATABASE_ID")
    GOOGLE_APPLICATION_CREDENTIALS: str = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

settings = Settings()
