import os
import threading
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .config import settings

# Configure Logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("DatabaseProvider")

class DatabaseProvider:
    """Thread-safe singleton for providing database engine and sessions."""
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DatabaseProvider, cls).__new__(cls)
                cls._instance._init_db()
            return cls._instance

    def _init_db(self):
        try:
            if settings.is_cloud and settings.database_url:
                db_url = settings.database_url
                if db_url.startswith("postgres://"):
                    db_url = db_url.replace("postgres://", "postgresql://", 1)
                logger.info("Initializing PostgreSQL for CLOUD_PROD environment.")
                self.engine = create_engine(db_url, pool_pre_ping=True, echo=False)
            else:
                os.makedirs(settings.data_dir, exist_ok=True)
                db_path = os.path.join(settings.data_dir, "oura_database.db")
                db_url = f"sqlite:///{db_path}"
                logger.info(f"Initializing SQLite for LOCAL_DEV environment at {db_path}.")
                self.engine = create_engine(
                    db_url,
                    connect_args={"check_same_thread": False},
                    echo=False
                )
            
            self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
            
            # Import models and initialize schema
            from ..models import Base
            Base.metadata.create_all(bind=self.engine)
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}")
            raise e

db_provider = DatabaseProvider()

def get_db():
    """FastAPI Dependency for database sessions."""
    db = db_provider.SessionLocal()
    try:
        yield db
    finally:
        db.close()
