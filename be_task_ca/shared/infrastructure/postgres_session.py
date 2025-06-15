from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from be_task_ca.shared.settings import settings
from sqlalchemy.orm import sessionmaker

engine = create_engine(settings.postgres_uri)
SessionLocal: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
