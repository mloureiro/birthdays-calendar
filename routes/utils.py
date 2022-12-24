from flask import redirect, request, session, url_for
from functools import wraps


def login_required(f):
  @wraps(f)
  def decorated_function(*args, **kwargs):
    if session.get("user_id") is None:
      return redirect(url_for("app.login", redirect=request.path))
    return f(*args, **kwargs)
  return decorated_function
