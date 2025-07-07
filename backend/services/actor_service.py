from bson import ObjectId
from extensions import mongo

def get_actors_by_filters(actor_name=None, movie_name=None, genre_name=None ):
    actor_ids = None

    if movie_name:
        movie = mongo.db.movies.find_one({'title': movie_name},collation={'locale': 'en', 'strength': 2})
        if not movie:
            return []
        actor_ids = set(movie['actor_ids'])

    if genre_name:
        genre = mongo.db.genres.find_one({'name': genre_name},collation={'locale': 'en', 'strength': 2})
        if not genre:
            return []

        genre_movies = mongo.db.movies.find({'genre_ids': genre['_id']})
        genre_actor_ids = set()
        for m in genre_movies:
            genre_actor_ids.update(m['actor_ids'])

        actor_ids = genre_actor_ids if actor_ids is None else actor_ids & genre_actor_ids

    if actor_name:
        actor = mongo.db.actors.find_one({'name': actor_name},collation={'locale': 'en', 'strength': 2})
        movies = list(mongo.db.movies.find({'actor_ids': actor['_id']}))
        movie_data = [{"_id": str(m["_id"]), "title": m["title"]} for m in movies]
        genre_ids = set(gid for m in movies for gid in m['genre_ids'])
        genres = list(mongo.db.genres.find({'_id': {'$in': list(genre_ids)}}))
        genre_names = [g['name'] for g in genres]
        result = []
        if not actor:
            return []
        result.append({
            "_id": str(actor['_id']),
            "name": actor['name'],
            "birth_year": actor['birth_year'],
            "country": actor['country'],
            "movies": movie_data,
            "genres": genre_names
        })

        return result

    actor_query = {}
    if actor_ids is not None:
        if not actor_ids:
            return []
        actor_query['_id'] = {'$in': list(actor_ids)}

    actors = list(mongo.db.actors.find(actor_query))
    result = []

    for actor in actors:
        movies = list(mongo.db.movies.find({'actor_ids': actor['_id']}))
        movie_data = [{"_id": str(m["_id"]), "title": m["title"]} for m in movies]

        genre_ids = set(gid for m in movies for gid in m['genre_ids'])
        genres = list(mongo.db.genres.find({'_id': {'$in': list(genre_ids)}}))
        genre_names = [g['name'] for g in genres]

        result.append({
            "_id": str(actor['_id']),
            "name": actor['name'],
            "birth_year": actor['birth_year'],
            "country": actor['country'],
            "movies": movie_data,
            "genres": genre_names
        })

    return result


def get_actor_by_id(actor_id):
    try:
        actor = mongo.db.actors.find_one({'_id': ObjectId(actor_id)})
        if not actor:
            return None
        movies = list(mongo.db.movies.find({'actor_ids': ObjectId(actor_id)}))

        movie_list = []
        genre_ids = set()

        for movie in movies:
            movie_list.append({
                "_id": str(movie["_id"]),
                "title": movie["title"]
            })
            genre_ids.update(movie.get('genre_ids', []))
        genres = list(mongo.db.genres.find({'_id': {'$in': list(genre_ids)}}))
        genre_names = [g['name'] for g in genres]

        return {
            "_id": str(actor['_id']),
            "name": actor['name'],
            "birth_year": actor.get("birth_year"),
            "country": actor.get("country"),
            "genres": genre_names,
            "movies": movie_list
        }

    except Exception as e:
        print(f"Error in get_actor_by_id: {e}")
        return None
    

def update_actor_by_name(name, data):
    actor = mongo.db.actors.find_one({'name': name})
    if not actor:
        return 404

    update_fields = {}
    if 'birth_year' in data:
        update_fields['birth_year'] = int(data['birth_year'])
    if 'country' in data:
        update_fields['country'] = data['country']

    mongo.db.actors.update_one({'_id': actor['_id']}, {'$set': update_fields})
    return True