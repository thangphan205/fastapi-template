from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from settings import settings

# Sqlite DB
engine = create_engine(
    "sqlite:///" + settings.SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
)
"""
Postgres DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)
"""
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


"""
engine = create_engine(settings.SQLALCHEMY_DATABASE_URI, pool_pre_ping=True)
db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

"""
