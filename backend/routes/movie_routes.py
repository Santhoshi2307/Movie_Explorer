from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.movie_service import get_all_movies,get_movie_by_id, add_movie
from schemas.movie_schema import MovieSchema
from marshmallow import ValidationError



movie_bp = Blueprint('movies', __name__)

@movie_bp.route('/movies', methods=['GET'])
@swag_from('../docs/movies_get.yml')  
def list_movies():
    filters = request.args.to_dict()
    movies = get_all_movies(filters)
    if not movies:
        return jsonify({"message": "No movies found matching the filters."}), 404
    return jsonify(movies)


@movie_bp.route('/movies/<movie_id>', methods=['GET'])
def get_movie_by_id_route(movie_id):
    movie = get_movie_by_id(movie_id)
    if not movie:
        return jsonify({"message": "Movie not found"}), 404
    return jsonify(movie)


@movie_bp.route('/movies', methods=['POST'])
@swag_from('../docs/movies_post.yml')
def add_movie_route():
    data = request.get_json()
    required_fields = ['title', 'release_year', 'director', 'actors', 'genres']
    if not all(field in data for field in required_fields):
        return jsonify({'error': 'Missing required fields'}), 400

    try:
        movie_id = add_movie(data)
        if movie_id == 409:
            return jsonify({'message': 'Movie already exists'}), 409

        return jsonify({'message': 'Movie added successfully', 'id': str(movie_id)}), 201

    except ValueError as ve:
        return jsonify({'error': str(ve)}), 400
    except Exception as e:
        print(f"Error in add_movie_route: {e}")
        return jsonify({'error': 'Internal server error'}), 500
