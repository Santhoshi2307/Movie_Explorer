from extensions import mongo


def get_movie_collection():
    return mongo.db.movies