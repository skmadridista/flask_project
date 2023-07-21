from flask import Flask
# from flask_migrate import Migrate
from config import Config
from app.extensions import db
from flask_login import LoginManager

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    with app.app_context():

    # Initialize Flask extensions here
        db.init_app(app)


    # Initialize Flask LoginManager here

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)


    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))




    # Initialize Flask-Migrate
    # migrate = Migrate(app, db)

    # Register blueprints here

    from app.main import main_bp,auth_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app