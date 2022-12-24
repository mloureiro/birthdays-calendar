class ValidationException(Exception):
  @staticmethod
  def by_message(message):
    return ValidationException(message or 'Invalid value')

  @staticmethod
  def by_key(key):
    return ValidationException(f"{key} is invalid")

  @staticmethod
  def by_value(key, value):
    return ValidationException(f"{key} with '{value}' is invalid")
