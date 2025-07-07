from extensions import mongo


def get_genre_collection():
    return mongo.db.genres