from sqlalchemy import (
    create_engine,
    )
from sqlalchemy.orm import sessionmaker

from src.constant import DATABASE_FILE

engine = create_engine(f"sqlite+pysqlite:///{DATABASE_FILE}")
Session = sessionmaker(bind=engine)
