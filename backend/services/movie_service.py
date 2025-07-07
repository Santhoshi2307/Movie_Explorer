from bson import ObjectId
from extensions import mongo
from pymongo.errors import DuplicateKeyError

def get_all_movies(filters):
    query = {}

    if 'title' in filters:
        movies = mongo.db.movies.find({'title':filters['title']},collation={'locale': 'en', 'strength': 2})
        result = []
        for movie in movies:
            director = mongo.db.directors.find_one({'_id': movie['director_id']})
            actors_cursor = mongo.db.actors.find({'_id': {'$in': movie['actor_ids']}})
            genres_cursor = mongo.db.genres.find({'_id': {'$in': movie['genre_ids']}})

            result.append({
                "_id": str(movie["_id"]),
                "title": movie.get("title"),
                "release_year": movie.get("release_year"),
                "director_id": str(movie.get("director_id")),
                "director_name": director["name"] if director else "Unknown",
                "actors": [{"_id": str(a["_id"]), "name": a["name"]} for a in actors_cursor],
                "genres": [g["name"] for g in genres_cursor]
            })
        return result

    if 'genre' in filters:
        genre = mongo.db.genres.find_one({'name': filters['genre']},collation={'locale': 'en', 'strength': 2})
        if genre:
            query['genre_ids'] = ObjectId(genre['_id'])
        else:
            return []

    if 'director' in filters:
        director = mongo.db.directors.find_one({'name': filters['director']},collation={'locale': 'en', 'strength': 2})
        if director:
            query['director_id'] = ObjectId(director['_id'])
        else:
            return []

    if 'actor' in filters:
        actor = mongo.db.actors.find_one({'name': filters['actor']},collation={'locale': 'en', 'strength': 2})
        if actor:
            query['actor_ids'] = ObjectId(actor['_id'])
        else:
            return []

    if 'release_year' in filters:
        query['release_year'] = int(filters['release_year'])

    movies = mongo.db.movies.find(query)
    result = []

    for movie in movies:
        director = mongo.db.directors.find_one({'_id': movie['director_id']})
        actors_cursor = mongo.db.actors.find({'_id': {'$in': movie['actor_ids']}})
        genres_cursor = mongo.db.genres.find({'_id': {'$in': movie['genre_ids']}})

        result.append({
            "_id": str(movie["_id"]),
            "title": movie.get("title"),
            "release_year": movie.get("release_year"),
            "director_id": str(movie.get("director_id")),
            "director_name": director["name"] if director else "Unknown",
            "actors": [{"_id": str(a["_id"]), "name": a["name"]} for a in actors_cursor],
            "genres": [g["name"] for g in genres_cursor]
        })

    return result


def get_movie_by_id(movie_id):
    try:
        movie = mongo.db.movies.find_one({'_id': ObjectId(movie_id)})
        director = mongo.db.directors.find_one({'_id': movie['director_id']})
        actors_cursor = mongo.db.actors.find({'_id': {'$in': movie['actor_ids']}})
        genres_cursor = mongo.db.genres.find({'_id': {'$in': movie['genre_ids']}})

        return{
            "_id": str(movie["_id"]),
            "title": movie.get("title"),
            "release_year": movie.get("release_year"),
            "director_id": str(movie.get("director_id")),
            "director_name": director["name"] if director else "Unknown",
            "actors": [{"_id": str(a["_id"]), "name": a["name"]} for a in actors_cursor],
            "genres": [g["name"] for g in genres_cursor]
        }
    except Exception as e:
        print(f"Error in get_movie_by_id: {e}")
        return None
    

def add_movie(data):
    try:
        title = data['title']
        release_year = int(data['release_year'])
        director_name = data['director']
        actor_names = data['actors']
        genre_names = data['genres']

        
        director = mongo.db.directors.find_one({'name': director_name})
        if not director:
            director_id = mongo.db.directors.insert_one({'name': director_name}).inserted_id
        else:
            director_id = director['_id']

        
        actor_ids = []
        for name in actor_names:
            actor = mongo.db.actors.find_one({'name': name})
            if not actor:
                actor_id = mongo.db.actors.insert_one({'name': name}).inserted_id
            else:
                actor_id = actor['_id']
            actor_ids.append(actor_id)

        
        genre_ids = []
        for name in genre_names:
            genre = mongo.db.genres.find_one({'name': name})
            if not genre:
                genre_id = mongo.db.genres.insert_one({'name': name}).inserted_id
            else:
                genre_id = genre['_id']
            genre_ids.append(genre_id)

        
        movie_doc = {
            'title': title,
            'release_year': release_year,
            'director_id': director_id,
            'actor_ids': actor_ids,
            'genre_ids': genre_ids
        }

        result = mongo.db.movies.insert_one(movie_doc)
        return result.inserted_id
    except DuplicateKeyError:
        return 409