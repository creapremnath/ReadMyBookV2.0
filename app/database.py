import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# import app.logs.rmblogger as logger

# # Create logger object
# logger = qtslogger.logger()

# SQLite database file path (use a relative or absolute path)
DATABASE_NAME = "infobase.db"  # Change this to your desired database filename

# Construct SQLite URL (SQLite is file-based, so the format is different)
DATABASE_URL = f"sqlite:///{DATABASE_NAME}"

# Function to check if the SQLite database exists (SQLite automatically creates it if it doesn't exist)
def check_and_create_db():
    # SQLite doesn't require manual creation of databases, it auto-creates the file when accessed.
    # So, we'll just log that we're ensuring the database exists
    try:
        conn = sqlite3.connect(DATABASE_NAME)
        # logger.info(f"SQLite database '{DATABASE_NAME}' is ready.")
        conn.close()
    except sqlite3.Error as e:
        # logger.error(f"Error connecting to SQLite database: {e}")
        raise

# Call the function to ensure the SQLite database is ready
check_and_create_db()

# Database engine for SQLite (using SQLAlchemy)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False}, pool_size=10, max_overflow=20)

# Session Maker (Workspace provider for SQLite)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Blueprint for the Databases (Declarative Base)
Base = declarative_base()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

get_db()