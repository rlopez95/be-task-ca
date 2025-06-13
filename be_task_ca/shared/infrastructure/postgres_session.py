from sqlalchemy import create_engine

from be_task_ca.settings import settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.postgres_uri)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
