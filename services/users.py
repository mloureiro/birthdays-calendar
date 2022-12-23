import bcrypt
from db import db
from services.utils import string_to_date, random_string
from services.validation import (
  is_valid_name,
  is_valid_email,
  is_valid_password,
  is_valid_birthdate,
)


def encrypt(password):
  return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())


def authenticate(email, password):
  try:
    user = get_user_by_email(email)
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

  if get_user_by_email(email) is not None:
    raise Exception("Email is already registered")

  db().execute(
    """
    INSERT INTO users 
      (email, password, public_id, birthdate, first_name, last_name) 
    VALUES (?,?,?,?,?,?)
    """,
    (email,
    encrypt(password).decode('utf-8'),
    random_string(),
    str(string_to_date(birthdate)),
    first_name,
    last_name))


def get_user_by_email(email):
  user_list = db().execute('SELECT * FROM user WHERE email = ?', (email,))
  if len(user_list) == 0:
    return None

  if len(user_list) == 1:
    return user_list[0]

  raise Exception('Expected 1 user but found %d' % len(user_list))


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

