from flask import Flask
from flasgger import Swagger
from flask_cors import CORS
import yaml
from extensions import mongo
from config import Config
from routes import register_blueprints
from schemas.movie_schema import MovieSchema
from schemas.actor_schema import ActorSchema




def create_app():
    app = Flask(__name__)
    CORS(app, origins=["http://localhost:5173"])
    app.config.from_object(Config)
    mongo.init_app(app)
    with open("docs/swagger_template.yml", "r") as f:
        swagger_template = yaml.safe_load(f)

    Swagger(app, template=swagger_template)
    register_blueprints(app)
    return app

if __name__ == '__main__':
    create_app().run(debug=True)