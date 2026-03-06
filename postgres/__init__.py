import logging

from sqlalchemy import create_engine

from postgres.postgres_db import Base

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
LOGGER = logging.getLogger(__name__)
def get_db_engine():
    engine = create_engine('postgresql+psycopg2://{}:{}@{}/{}'.format('postgres', 'postgres', 'localhost:5432', 'bamba_db'))
    Base.metadata.create_all(engine)
    return engine
while True:
    try:
        db_engine = get_db_engine().connect()
        if db_engine:
            break
    except Exception as e:
        LOGGER.warning(f"++++ Retrying connection to the database because of the issue {str(e)}++++")
        print(e, "🤖")
