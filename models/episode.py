from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine

episodes = Table(
    "episodes",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("air_date", String(255)),
    Column("episode", String(255)),
)

meta.create_all(engine)
