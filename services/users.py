from db import db
import validation


def register(email, password, birthdate):
  if (
    not validation.is_valid_email(email)
    or not validation.is_valid_password(password)
    or not validation.is_valid_birthdate(birthdate)
  ):
    raise Exception("Invalid user values")

  if get_by_email(email) is not None:
    raise Exception("Existing user")

  db().execute(
    "INSERT INTO users (email, password, key, birthdate)VALUES (?, ?, ?)",
    email,
    password,
    birthdate)


def get_by_email(email):
  try:
    user_list = db().execute('SELECT * FROM user WHERE email = ?', email)
    if len(user_list) != 1:
      raise Exception('Expected 1 user but found %d' % len(user_list))

    return user_list[0]
  except:
    return None
