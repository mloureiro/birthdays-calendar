from os import environ
from cs50 import SQL

_conn = None

def db():
  global _conn
  if (_conn == None):
    _conn = SQL("postgresql+psycopg2://{user}:{pwd}@{host}:{port}/{name}"\
      .format(
        user=environ["DATABASE_USER"],
        pwd=environ["DATABASE_PASS"],
        host=environ["DATABASE_HOST"],
        port=environ["DATABASE_PORT"],
        name=environ["DATABASE_NAME"]))
    
  return _conn
