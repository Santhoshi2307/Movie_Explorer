from extensions import mongo


def get_actor_collection():
    return mongo.db.actors