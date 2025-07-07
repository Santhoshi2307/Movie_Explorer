from marshmallow import Schema, fields

class ActorSchema(Schema):
    _id = fields.String(dump_only=True)
    name = fields.String(required=True)
    birth_year = fields.Integer(required=True)
    country = fields.String(required=True)