from pathlib import Path
from app.core.settings import settings

PROJECT_ROOT = Path(__file__).resolve().parents[2]

STORAGE_DIR = PROJECT_ROOT / "storage"

DOCUMENTS_DIR = settings.documents_path

CHROMA_DIR = settings.chroma_path

STORAGE_DIR = settings.storage_path

UPLOADS_DIR = STORAGE_DIR / "uploads"

TEMP_DIR = STORAGE_DIR / "temp"

DOCUMENTS_DIR.mkdir(parents=True, exist_ok=True)
UPLOADS_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)