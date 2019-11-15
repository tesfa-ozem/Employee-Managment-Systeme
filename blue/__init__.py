import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    from blue.api.routes import mod as mod
    app.register_blueprint(mod)

    return app


from blue import models
