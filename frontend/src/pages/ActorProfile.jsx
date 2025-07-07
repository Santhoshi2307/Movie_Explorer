import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const ActorProfile = () => {
  const { id } = useParams(); // Get actor ID from URL
  const [actor, setActor] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchActor = async () => {
      try {
        const res = await axios.get(`http://localhost:5000/actors/${id}`);
        setActor(res.data);
      } catch (error) {
        console.error('Error fetching actor:', error);
        setActor(null);
      } finally {
        setLoading(false);
      }
    };

    fetchActor();
  }, [id]);

  if (loading) return <p>Loading actor profile...</p>;
  if (!actor) return <p>Actor not found.</p>;

  return (
    <div className="container mt-4">
      <h2>{actor.name}</h2>
      <p><strong>Birth Year:</strong> {actor.birth_year}</p>
      <p><strong>Country:</strong> {actor.country}</p>

      <h4>Genres</h4>
      <ul>
        {actor.genres.map((genre, idx) => (
          <li key={idx}>{genre}</li>
        ))}
      </ul>

      <h4>Movies</h4>
      <ul>
        {actor.movies.map((movie) => (
          <li key={movie._id}>
            <Link className="text-decoration-none" to={`/movie/${movie._id}`}>{movie.title}</Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ActorProfile;