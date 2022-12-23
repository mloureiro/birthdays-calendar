import re
from datetime import datetime

DEFAULT_DATE_FORMAT = '%Y-%m-%d'


def is_valid_email(email):
  return re.fullmatch(
    r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
    email)


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
    date = datetime.strptime(date, DEFAULT_DATE_FORMAT).date()
    return date < datetime.now()
  except:
    return False
