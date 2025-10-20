from app import app
from app.auth import bp as auth_bp
from app.main import bp as main_bp

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(main_bp)