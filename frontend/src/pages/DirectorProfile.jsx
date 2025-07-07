import React, { useEffect, useState } from 'react';
import { useParams, Link } from 'react-router-dom';
import axios from 'axios';

const DirectorProfile = () => {
  const { id } = useParams();  // Get director ID from URL
  const [director, setDirector] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchDirector = async () => {
      try {
        const res = await axios.get(`http://localhost:5000/directors/${id}`);
        setDirector(res.data);
      } catch (error) {
        console.error('Error fetching director:', error);
        setDirector(null);
      } finally {
        setLoading(false);
      }
    };

    fetchDirector();
  }, [id]);

  if (loading) return <p>Loading director profile...</p>;
  if (!director) return <p>Director not found.</p>;

  return (
    <div className="container mt-4">
      <h2>{director.name}</h2>
      <p><strong>Birth Year:</strong> {director.birth_year}</p>
      <p><strong>Country:</strong> {director.country}</p>

      <h4>Genres</h4>
      <ul>
        {director.genres.map((genre, idx) => (
          <li key={idx}>{genre}</li>
        ))}
      </ul>

      <h4>Movies</h4>
      <ul>
        {director.movies.map((movie) => (
          <li key={movie._id}>
                      <Link  className="text-decoration-none" to={`/movie/${movie._id}`}>{movie.title}</Link>
                    </li>
        ))}
      </ul>
    </div>
  );
};

export default DirectorProfile;