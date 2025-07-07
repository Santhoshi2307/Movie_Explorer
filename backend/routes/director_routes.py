from flask import Blueprint, request, jsonify
from flasgger import swag_from
from services.director_service import get_director,get_director_by_id, update_director_by_name




director_bp = Blueprint('directors', __name__)

@director_bp.route('/directors', methods=['GET'])
@swag_from('../docs/directors_get.yml')
def list_actors():
    name = request.args.get('name')

    directors = get_director(name=name)

    if not directors:
        return jsonify({"message": "No Directors found matching the filters."}), 404

    return jsonify(directors)

@director_bp.route('/directors/<director_id>', methods=['GET'])
def get_director_by_id_route(director_id):
    director = get_director_by_id(director_id)
    if not director:
        return jsonify({"message": "Director not found"}), 404
    return jsonify(director)


@director_bp.route('/directors/<name>', methods=['PUT'])
@swag_from('../docs/director_put.yml')
def update_director_route(name):
    data = request.get_json()
    updated = update_director_by_name(name, data)
    if updated == 404:
        return jsonify({"error": "Director not found"}), 404
    return jsonify({"message": "Director updated successfully"}), 200