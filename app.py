from dotenv import load_dotenv
from flask import Flask
from routes.app import app as routes_app
from routes.api import api as routes_api

load_dotenv()

flask_app = Flask(__name__)

flask_app.register_blueprint(routes_app)
flask_app.register_blueprint(routes_api, url_prefix='/api')

if __name__ == '__main__':
  flask_app.debug = True
  flask_app.run()


# vercel requires 'app' to be the final export
app = flask_app
