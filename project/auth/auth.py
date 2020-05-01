import flask

auth_bp = flask.Blueprint('auth', __name__)

@auth_bp.route('/login')
def login():
    return "login"

@auth_bp.route('/signup')
def signup():
    return "signup"
