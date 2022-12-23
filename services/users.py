import bcrypt
from db import db
import validation


def encrypt(password):
  return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def authenticate(email, password):
  try:
    user = get_by_email(email)
    if (user is None
      or not bcrypt.checkpw(
        password.encode('utf-8'),
        user.password.encode('utf-8'))):
      raise Exception()
  except:
    raise Exception('Unauthorized')


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
    encrypt(password),
    birthdate)


def get_by_email(email):
  try:
    user_list = db().execute('SELECT * FROM user WHERE email = ?', email)
    if len(user_list) != 1:
      raise Exception('Expected 1 user but found %d' % len(user_list))

    return user_list[0]
  except:
    return False


def validate_user_details(first_name, last_name, email, password, birthdate):
  if not is_valid_name(first_name):
    raise UserDetailsInvalidException("Name", first_name)
  if not is_valid_name(last_name):
    raise UserDetailsInvalidException("Name", last_name)
  if not is_valid_email(email):
    raise UserDetailsInvalidException("Email", email)
  if not is_valid_password(password, strict=False):
    raise UserDetailsInvalidException("Password")
  if not is_valid_birthdate(birthdate):
    raise UserDetailsInvalidException("Birthdate", birthdate)


class UserDetailsInvalidException(Exception):
  def __init__(self, key, value=None, *args):
    message = f"{key} is invalid" if value is None else f"{key} as '{value}' is invalid"
    print('[message]>>', message)
    super().__init__(message, args)

