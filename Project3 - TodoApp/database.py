import os
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import Boolean, Column, DateTime, Integer, String, create_engine
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Mapped, declarative_base, mapped_column, sessionmaker

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("❌ DATABASE_URL not found in environment variables.")

# 1. Create Base
Base = declarative_base()

# 2. IMPORT THE MODEL - FIX THE IMPORT PATH!
# Since database.py and models/ are in the same folder:
# from models.todo import Todo  # ← This is the correct import

# 3. Create engine
engine = create_engine(DATABASE_URL, echo=True)

# 4. Create session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[Optional[str]] = mapped_column(String, nullable=True)
    completed: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )


def create_tables():
    """Create all tables in the database."""
    try:
        Base.metadata.create_all(bind=engine)
        print("✅ Tables created successfully!")
        return True
    except SQLAlchemyError as e:
        print(f"❌ Failed to create tables: {e}")
        return False


if __name__ == "__main__":
    create_tables()
