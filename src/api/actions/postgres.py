import datetime

from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import sessionmaker
import uuid

from postgres.postgres_db import Bamba, Status
from src.api.modules.deployment import Dep

engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'bamba_db'))
Session = sessionmaker(bind=engine)
session = Session()
def add_database(db_name: str, username: str):
    id = str(uuid.uuid4())
    session.add(Bamba(id=id, db_name="matmon15-" + db_name, status=Status.CREATED, username=username, creation_time=datetime.datetime.now()))
    print(Bamba(id=id, db_name="matmon15-" + db_name, status=Status.CREATED, username=username, creation_time=datetime.datetime.now()))
    session.commit()
    return id

def get_database(id: str):
    stmt = select(Bamba).where(Bamba.id == id)
    db = session.scalar(stmt)
    deployment_data = {"id": db.id, "db_name": db.db_name, "status": db.status, "creation_time": db.creation_time}
    return deployment_data



def update_db_name(deployment_id: str, dep: Dep):
    stmt = (update(Bamba).where(Bamba.id == deployment_id).values(db_name="matmon15-" + dep.db_name))
    session.execute(stmt)
    session.commit()
    return deployment_id



