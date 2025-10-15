from google.cloud import firestore
from app.config import settings

# Obtener configuración desde settings
project_id = settings.GCP_PROJECT_ID
database_id = settings.FIRESTORE_DATABASE_ID

# Validar que estén configurados
if not project_id:
    raise ValueError("GCP_PROJECT_ID no está configurado")
if not database_id:
    raise ValueError("FIRESTORE_DATABASE_ID no está configurado")

# Inicializar cliente de Firestore
client = firestore.Client(project=project_id, database=database_id)

# Función para obtener el cliente
def get_firestore_client():
    return client
