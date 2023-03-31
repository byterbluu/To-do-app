from flask import Flask, render_template

def create_app():
    app = Flask(__name__)

    # APP CONFIGURER
    app.config.from_mapping(
        DEBUG = True,
        SECRET_KEY = 'dev',
    )

    # BLUEPRINT REGISTER
    from . import todo
    app.register_blueprint(todo.bp)

    from . import auth
    app.register_blueprint(auth.bp)



    @app.route('/')
    def index():
        return render_template('index.html')
    return app

