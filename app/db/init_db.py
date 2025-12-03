from app.db.session import engine
from app.db.base import Base

# 🔽 Імпортуємо всі моделі, щоб вони зареєструвались у Base.metadata
from app.models.request import Request
from app.models.logs import ProcessingLog
from app.models.diagnostics import Diagnostics
from app.models.reports import Report

def init_db():
    Base.metadata.create_all(bind=engine)
