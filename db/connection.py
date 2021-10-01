import databases
import sqlalchemy

from db.models import metadata

DATABASE_URL = "sqlite:///./blogapi.db"
database = databases.Database(DATABASE_URL)
engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

metadata.create_all(engine)
