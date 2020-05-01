from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_manager

# init SQLAlchemy so we can use it later in our models


db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)




    app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    register_extensions(app)
    register_blueprints(app)


    return app


def register_extensions(app):
    print("registering extensions")
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    from .models import User
    print("test")
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    # blueprint for auth routes in our app
    from .auth.auth import auth_bp
    app.register_blueprint(auth_bp)
    from .main.main import main_bp
    app.register_blueprint(main_bp)
    # blueprint for non-auth parts of app
    # from .main import main as main_blueprint
    # app.register_blueprint(main_blueprint)
    from .cal.cal import calendar_bp
    app.register_blueprint(calendar_bp, url_prefix='/calendar')
    print("test this")

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True,host='0.0.0.0', port=5000)

    print("main running")
