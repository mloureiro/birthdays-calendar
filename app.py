from dotenv import load_dotenv
from flask import Flask
from routes.app import app
from routes.api import api

load_dotenv()

flaskApp = Flask(__name__)

flaskApp.register_blueprint(app)
flaskApp.register_blueprint(api, url_prefix='/api')

if __name__=='__main__':
  flaskApp.debug=True
  flaskApp.run()
