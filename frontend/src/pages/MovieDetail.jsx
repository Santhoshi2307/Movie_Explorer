import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const MovieDetail = () => {
  const { id } = useParams(); // get movie ID from the URL
  const [movie, setMovie] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchMovie = async () => {
      try {
        const res = await axios.get(`http://localhost:5000/movies/${id}`);
        setMovie(res.data);
      } catch (error) {
        console.error('Error fetching movie:', error);
        setMovie(null);
      } finally {
        setLoading(false);
      }
    };

    fetchMovie();
  }, [id]);

  if (loading) return <p>Loading movie details...</p>;
  if (!movie) return <p>Movie not found.</p>;

  return (
    <div className="container mt-4">
      <h2>{movie.title}</h2>
      <p><strong>Release Year:</strong> {movie.release_year}</p>
      <p>
        <strong>Director:</strong>{' '}
        <Link className="text-decoration-none" to={`/director/${movie.director_id}`}>{movie.director_name}</Link>
      </p>

      <h4>Genres</h4>
      <ul>
        {movie.genres.map((genre, idx) => (
          <li key={idx}>{genre}</li>
        ))}
      </ul>

      <h4>Actors</h4>
      <ul>
        {movie.actors.map((actor) => (
          <li key={actor._id}>
            <Link className="text-decoration-none" to={`/actor/${actor._id}`}>{actor.name}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default MovieDetail;