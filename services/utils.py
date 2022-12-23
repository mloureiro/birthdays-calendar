from random import choice
import string
from datetime import datetime

DEFAULT_DATE_FORMAT = '%d/%m/%Y'

DEFAULT_CHARACTER_LIST = string.ascii_letters + string.digits


def string_to_date(date_string):
  return datetime.strptime(date_string, DEFAULT_DATE_FORMAT).date()


def random_string(length=8, character_list=DEFAULT_CHARACTER_LIST):
  return ''.join(choice(string.ascii_letters + string.digits) for _ in range(length))
