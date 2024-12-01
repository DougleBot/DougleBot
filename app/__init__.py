from flask import Flask

def create_app():
    app = Flask(__name__)

    # Register routes
    with app.app_context():
        from .routes import main
        app.register_blueprint(main)  # This line is now correctly indented within the block

    return app
