import re
from datetime import datetime
from services.utils import string_to_date


def is_valid_name(name):
  return bool(re.fullmatch(r'\b([\w+\-\.]+\s?)+\b', name))


def is_valid_email(email):
  return bool(re.fullmatch(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    email))


def is_valid_password(pwd, strict=True):
  return (len(pwd) > 8
    # has an upper case letter
    and bool(re.search(r"[A-Z]", pwd))
    # has a lower case letter
    and bool(re.search(r"[a-z]", pwd))
    and (
        not strict
        or (
          # has a digit
          bool(re.search(r"\d", pwd))
          # has a special character
          and bool(re.search(r"[ !#$%&'()*+,-./[\\\]^_`{|}~"+r'"]', pwd)))
        ))


def is_valid_birthdate(date):
  try:
    return string_to_date(date) < datetime.now().date()
  except:
    return False
