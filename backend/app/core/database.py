from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# -------------------------------------------------
# PostgreSQL Database URL
# -------------------------------------------------
DATABASE_URL = "postgresql://postgres:forgot_123@localhost:5432/nutricart"

# -------------------------------------------------
# SQLAlchemy Engine
# -------------------------------------------------
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True
)

# -------------------------------------------------
# Session factory
# -------------------------------------------------
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# -------------------------------------------------
# Base class for models
# -------------------------------------------------
Base = declarative_base()

# -------------------------------------------------
# DB dependency
# -------------------------------------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
