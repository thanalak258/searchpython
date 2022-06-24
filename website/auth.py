from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/search')
def search():
    return "<p>Search</p>"