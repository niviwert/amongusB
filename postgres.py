import sqlalchemy.orm
from sqlalchemy import create_engine, schema
from sqlalchemy import text
from faker import Faker
import logging, time

from sqlalchemy.engine import create

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)

#create_engine => username, password, hostname:port, database
def get_db_engine():
    return create_engine('postgresql://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'bamba_db' ) )
#retry mechanism for connect to database
while True:
    try:
        db_engine = get_db_engine().connect()
        if db_engine:
            break
    except Exception as e:
        LOGGER.warning(f"++++ Retrying connection to the database because of the issue {str(e)}++++")
        print(e, "🤖")


from enum import Enum

class Status(Enum) :
    CREATED = 'created'
    DELETED = 'deleted'

from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase

metadata_obj = MetaData(schema="{}")


class Base(DeclarativeBase):
    metadata = metadata_obj


class Bamba1(Base):
    # will use "some_schema" by default
    __tablename__ = "amongus"
    __table_args__ = {"schema": "some_schema"}



