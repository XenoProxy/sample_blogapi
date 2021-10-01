import sqlalchemy
metadata = sqlalchemy.MetaData()

post = sqlalchemy.Table(
    "posts",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.INTEGER, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("is_published", sqlalchemy.Boolean),
)
