from flask import Flask

def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = '37280d7558dcb27f84d64d6d91b8bb85ad2c0318b43fa894cea442ed154211e8'

    from app.auth import bp as auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

