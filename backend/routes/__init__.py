from .movie_routes import movie_bp
from .actor_routes import actor_bp
from .director_routes import director_bp


def register_blueprints(app):
    app.register_blueprint(movie_bp)
    app.register_blueprint(actor_bp)
    app.register_blueprint(director_bp)