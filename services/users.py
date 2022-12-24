import bcrypt
from db import db
from services.utils import string_to_date, random_string
import services.validation as validation
from services.exceptions import ValidationException;


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


def register_user(first_name, last_name, email, password, birthdate):
  validate_user_details(first_name, last_name, email, password, birthdate)

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
  if not validation.is_valid_name(first_name):
    raise ValidationException.by_value("Name", first_name)
  if not validation.is_valid_name(last_name):
    raise ValidationException.by_value("Name", last_name)
  if not validation.is_valid_email(email):
    raise ValidationException.by_value("Email", email)
  if not validation.is_valid_password(password, strict=False):
    raise ValidationException.by_key("Password")
  if not validation.is_valid_birthdate(birthdate):
    raise ValidationException.by_value("Birthdate", birthdate)
