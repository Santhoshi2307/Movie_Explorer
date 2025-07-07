from bson import ObjectId
from extensions import mongo

def get_director_by_id(director_id):
    try:
        director = mongo.db.directors.find_one({'_id': ObjectId(director_id)},collation={'locale': 'en', 'strength': 2})
        if not director:
            return None
        movies = list(mongo.db.movies.find({'director_id': ObjectId(director_id)}))
        genre_ids = set()
        movie_list = []
        for movie in movies:
            genre_ids.update(movie.get('genre_ids', []))
            movie_list.append({
                "_id": str(movie["_id"]),
                "title": movie["title"]
            })
        genre_ids = set(gid for m in movies for gid in m['genre_ids'])
        genres = list(mongo.db.genres.find({'_id': {'$in': list(genre_ids)}}))
        genre_names = [g['name'] for g in genres]
        return {
            "_id": str(director['_id']),
            "name": director['name'],
            "birth_year": director.get("birth_year"),
            "country": director.get("country"),
            "genres": genre_names,
            "movies": movie_list
        }

    except Exception as e:
        print(f"Error in get_director_by_id: {e}")
        return None

def get_director(name=None):
    director_name = name
    if director_name:
        director = mongo.db.directors.find_one({'name': director_name},collation={'locale': 'en', 'strength': 2})
        movies = list(mongo.db.movies.find({'director_id': director['_id']}))
        movie_data = [{"_id": str(m["_id"]), "title": m["title"]} for m in movies]
        genre_ids = set(gid for m in movies for gid in m['genre_ids'])
        genres = list(mongo.db.genres.find({'_id': {'$in': list(genre_ids)}}))
        genre_names = [g['name'] for g in genres]
        result = []
        if not director:
            return []
        result.append({
            "_id": str(director['_id']),
            "name": director['name'],
            "birth_year": director['birth_year'],
            "country": director['country'],
            "movies": movie_data,
            "genres": genre_names
        })
        return result
    
    directors = list(mongo.db.directors.find())
    result = []

    for director in directors:
        movies = list(mongo.db.movies.find({'director_id': director['_id']}))
        movie_data = [{"_id": str(m["_id"]), "title": m["title"]} for m in movies]

        genre_ids = set(gid for m in movies for gid in m['genre_ids'])
        genres = list(mongo.db.genres.find({'_id': {'$in': list(genre_ids)}}))
        genre_names = [g['name'] for g in genres]

        result.append({
           "_id": str(director['_id']),
            "name": director['name'],
            "birth_year": director['birth_year'],
            "country": director['country'],
            "movies": movie_data,
            "genres": genre_names
        })

    return result


def update_director_by_name(name, data):
    director = mongo.db.directors.find_one({'name': name})
    if not director:
        return 404

    update_fields = {}
    if 'birth_year' in data:
        update_fields['birth_year'] = int(data['birth_year'])
    if 'country' in data:
        update_fields['country'] = data['country']

    mongo.db.directors.update_one({'_id': director['_id']}, {'$set': update_fields})
    return True
