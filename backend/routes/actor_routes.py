from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.actor_service import get_actors_by_filters, get_actor_by_id, update_actor_by_name
from schemas.actor_schema import ActorSchema



actor_bp = Blueprint('actors', __name__)

@actor_bp.route('/actors', methods=['GET'])
@swag_from('../docs/actors_get.yml')
def list_actors():
    movie = request.args.get('movie')
    genre = request.args.get('genre')
    name = request.args.get('name')

    actors = get_actors_by_filters(actor_name=name,movie_name=movie, genre_name=genre)

    if not actors:
        return jsonify({"message": "No actors found matching the filters."}), 404

    return jsonify(actors)

@actor_bp.route('/actors/<actor_id>', methods=['GET'])
def get_actor_by_id_route(actor_id):
    actor = get_actor_by_id(actor_id)
    if not actor:
        return jsonify({"message": "Actor not found"}), 404
    return jsonify(actor)


@actor_bp.route('/actors/<name>', methods=['PUT'])
@swag_from('../docs/actor_put.yml')
def update_actor_route(name):
    data = request.get_json()
    updated = update_actor_by_name(name, data)
    if updated == 404:
        return jsonify({"error": "Actor not found"}), 404
    return jsonify({"message": "Actor updated successfully"}), 200