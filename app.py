import os

from flask import Flask, render_template
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from flask_smorest import Api, Blueprint, abort
import warnings

class Base(DeclarativeBase):
    pass


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy(model_class=Base)
ma = Marshmallow()

def create_app():
    warnings.filterwarnings(
        "ignore",
        message="Multiple schemas resolved to the name "
    )
    from tasks.models import Task
    from tasks.serializers import TaskSchema

    app = Flask(__name__)
    CORS(app)

    @app.route('/')
    def index():
        return '<h1>ECM Bonjour</h1>'

    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)

    @app.route('/professor')
    def my_api_route():
        return {
            "name": "Adrien",
            "birthday": "02 January",
            "age": 85,
            "sex": None,
            "friends": ["Amadou", "Mariam"]
        }

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['API_TITLE'] = 'My ECM API'
    app.config["API_VERSION"] = "1"
    app.config["OPENAPI_VERSION"] = "3.0.2"
    app.config["OPENAPI_URL_PREFIX"] = "/openapi"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/api"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"

    db.init_app(app)
    api = Api(app)
    ma.init_app(app)

    Migrate(app, db)

    from tasks.views import task_blueprint
    api.register_blueprint(task_blueprint)

    return app
