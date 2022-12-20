from flask import Blueprint, make_response
from db import reset_db as db_reset_db

api = Blueprint('api', __name__)

@api.route('/')
def main():
  return 'api'

@api.route('/reset-db/<pwd>', methods=['POST'])
def reset_db(pwd):
  try:
    db_reset_db(pwd)
    return make_response('Done', 204)
  except:
    return make_response('Not found', 404)
