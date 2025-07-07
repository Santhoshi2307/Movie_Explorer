from marshmallow import Schema, fields

class MovieSchema(Schema):
    _id = fields.String(dump_only=True)
    title = fields.String(required=True)
    release_year = fields.Integer(required=True)
    director_id = fields.String(required=True)
    actor_ids = fields.List(fields.String(), required=True)
    genre_ids = fields.List(fields.String(), required=True)