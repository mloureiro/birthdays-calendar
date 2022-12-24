from flask import (
  Blueprint,
  render_template,
  redirect,
  request,
  url_for
)
from services.exceptions import ValidationException
from services.users import (
  register_user,
  validate_user_details
)
from routes.utils import login_required

app = Blueprint("app", __name__)


@app.route("/", methods=["GET"])
@login_required
def main():
  return "main"


@app.route("/list", methods=["GET"])
@login_required
def birthday_list():
  return "list"


@app.route("/add/<user_key>", methods=["GET", "POST"])
@login_required
def add(user_key):
  return "add"


# AUTH

@app.route("/login", methods=["GET", "POST"])
def login():
  return "login"


@app.route("/logout", methods=["POST"])
def logout():
  return "logout"


@app.route("/register", methods=["GET", "POST"])
def register():
  if request.method == "GET":
    return render_template("auth/register.html")

  first_name = request.form['first_name']
  last_name = request.form['last_name']
  birthday = request.form['birthday']
  terms_and_conditions = request.form['terms_and_conditions']
  email = request.form['email']
  password = request.form['password']
  password_confirmation = request.form['password_confirmation']

  try:
    if not terms_and_conditions:
      raise ValidationException.by_message('Terms and conditions must be accepted')

    if not password == password_confirmation:
      raise ValidationException.by_message('Password and confirmation do not match')

    validate_user_details(first_name, last_name, email, password, birthday)
    register_user(first_name, last_name, email, password, birthday)

    return redirect(url_for('app.register', success=email))
  except ValidationException as error:
    return redirect(url_for('app.register',
      failure=str(error),
      first_name=first_name,
      last_name=last_name,
      birthday=birthday,
      email=email,
    ))
