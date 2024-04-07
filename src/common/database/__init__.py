from sqlalchemy import (
    create_engine,
)
from sqlalchemy.orm import Session as SType, sessionmaker

from src.core.constant import DATABASE_FILE

engine = create_engine(f"sqlite+pysqlite:///{DATABASE_FILE}")
sessionmaker = sessionmaker(bind=engine, autoflush=True)
Session = sessionmaker()


def get_session() -> SType:
    return Session
