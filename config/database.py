from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

postgres_password = config('PASSWORD_POSTGRES', cast=int)
database = config('DATABASE_NAME')

POSTGRES_DATABASE_URL = f"postgresql://postgres:{postgres_password}@localhost/{database}"
engine = create_engine(POSTGRES_DATABASE_URL)

# SQLITE_DATABASE_URL = "sqlite:///./blx.db"
# engine = create_engine(
#     SQLITE_DATABASE_URL, connect_args={'check_same_thread': False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def create_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()