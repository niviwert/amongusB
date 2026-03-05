import datetime

from sqlalchemy import create_engine
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.orm import sessionmaker
from uuid import uuid4

from src.api.modules.postgres.postgres_db import Bamba, Status

engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'bamba_db'))

def add_database(db_name: str, username: str):
    id = uuid4()
    Session = sessionmaker(bind=engine)
    session = Session()
    session.add(Bamba(id=id, db_name="matmon15-" + db_name, status=Status.CREATED, username=username, creation_time=datetime.now()))
    session.commit()
    return id