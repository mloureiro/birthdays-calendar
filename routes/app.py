from flask import Blueprint

app = Blueprint('app', __name__)


@app.route('/', methods=['GET'])
def main():
  return 'main'


@app.route('/list', methods=['GET'])
def birthday_list():
  return 'list'


@app.route('/add/<user_key>', methods=['POST'])
def add(user_key):
  return 'add'


# AUTH

@app.route('/login', methods=['GET', 'POST'])
def login():
  return 'login'


@app.route('/logout', methods=['POST'])
def logout():
  return 'logout'


@app.route('/register', methods=['GET', 'POST'])
def register():
  return 'register'
