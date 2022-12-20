import contextlib
from os import environ
from sqlalchemy import (
  Column,
  Date,
  DateTime,
  ForeignKey,
  Integer,
  MetaData,
  String,
  Table,
  create_engine,
  func
)


_meta = None
_engine = None


def engine():
  global _engine
  if (_engine == None):
    print('>>>', generate_db_url())
    _engine = create_engine(generate_db_url(), echo = True)

  return _engine


def db():
  return engine().connect()


def meta():
  global _meta
  if (_meta == None):
    _meta = MetaData()
    table_definition_users(_meta)
    table_definition_birthdays(_meta)

  return _meta


def generate_db_url():
  return get_db_url_template(environ.get("DATABASE_TYPE"))\
    .format(
      user=environ.get("DATABASE_USER"),
      pwd=environ.get("DATABASE_PASS"),
      host=environ.get("DATABASE_HOST"),
      port=environ.get("DATABASE_PORT"),
      name=environ.get("DATABASE_NAME"))


def get_db_url_template(type):
  type = type.lower()
  if (type == "sqlite"):
    return "sqlite:///{name}.db"

  if (type == "postgresql"):
    return "postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{name}"

  raise Exception("DB type '%s' is not supported" % type)


def reset_db(pwd):
  if not pwd or pwd != environ['DATABASE_RESET_KEY']:
    raise Exception("DB operation not supported")

  meta().drop_all(engine())
  meta().create_all(engine());


def table_definition_users(meta):
  return Table(
    'users', meta,

    Column('id', Integer, primary_key = True, autoincrement = True),
    Column('email', String(200), nullable = False, unique = True),

    Column('first_name', String(100), nullable = False),
    Column('last_name', String(100), nullable = False),
    Column('birthday', Date, nullable = False),

    Column('password', String(200), nullable = False),
    Column('public_id', String(20), nullable = True),

    Column('created_on', DateTime, default=func.now()),
    Column('updated_on', DateTime, default=func.now(), onupdate=func.now()),
  )


def table_definition_birthdays(meta):
  return Table(
    'birthdays', meta,

    Column('id', Integer, primary_key = True, autoincrement = True),
    Column('email', String(200), nullable = False, unique = True),

    Column('first_name', String(100), nullable = False),
    Column('last_name', String(100), nullable = False),
    Column('birthday', Date, nullable = False),

    Column('owner_id', Integer, ForeignKey("users.id"), nullable = False),

    Column('created_on', DateTime, default=func.now()),
    Column('updated_on', DateTime, default=func.now(), onupdate=func.now()),
  )
