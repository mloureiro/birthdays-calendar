from flask import (
  Blueprint,
  render_template,
  redirect,
  request,
  url_for
)
from services.users import (
  UserDetailsInvalidException,
  register_user,
  validate_user_details
)

app = Blueprint("app", __name__)


@app.route("/", methods=["GET"])
def main():
  return render_template("auth.register.html")


@app.route("/list", methods=["GET"])
def birthday_list():
  return "list"


@app.route("/add/<user_key>", methods=["POST"])
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
      raise UserDetailsInvalidException('Terms and conditions must be accepted')

    if not password == password_confirmation:
      raise UserDetailsInvalidException('Password and confirmation must match')

    validate_user_details(first_name, last_name, email, password, birthday)
    register_user(first_name, last_name, email, password, birthday)

    return redirect(url_for('app.register', success=email))
  except UserDetailsInvalidException as error:
    return redirect(url_for('app.register', failed=str(error)))
