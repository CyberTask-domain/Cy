from flask import Flask


def create_app():
    app = Flask(__name__)

    # Register blueprints
    # from yourapp.blueprints import your_blueprint
    # app.register_blueprint(your_blueprint)

    # Additional configuration can go here

    return app
