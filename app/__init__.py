from flask import Flask
from app.routes import home, dashboard, api
from app.db import init_db
from app.utils import filters
import os

def create_app(test_config=None):
    app = Flask(__name__, static_url_path='/')
    app.url_map.strict_slashes = False

    # Load configuration from environment variables or a .env file
    app.config.from_mapping(
        SECRET_KEY=os.getenv('SECRET_KEY'),
        SQLALCHEMY_DATABASE_URI=os.getenv('DB_URL'),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
    )

    # Register custom Jinja filters
    app.jinja_env.filters['format_url'] = filters.format_url
    app.jinja_env.filters['format_date'] = filters.format_date
    app.jinja_env.filters['format_plural'] = filters.format_plural

    # Example route
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Register blueprints
    app.register_blueprint(home)
    app.register_blueprint(dashboard)
    app.register_blueprint(api)

    # Initialize database
    init_db(app)

    return app
