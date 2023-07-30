from sqlalchemy.orm import Session

from src.config.db import Base, SessionLocal
from src.db import models

db: Session = SessionLocal()

__all__ = ["db", "Base", "models"]
