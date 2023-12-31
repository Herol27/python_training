from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .config import DB_USER, DB_NAME, DB_PORT, DB_HOST, DB_PASS

SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
