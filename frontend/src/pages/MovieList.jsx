import React, { useEffect, useState, useCallback } from 'react';
import axios from 'axios';
import { Link } from 'react-router-dom';
import debounce from 'lodash/debounce';

export default function MovieList() {
  const [movies, setMovies] = useState([]);
  const [filters, setFilters] = useState({ director: '', actor: '', genre: '' });
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  const fetchMovies = useCallback(
    debounce(async (filters) => {
      try {
        setLoading(true);

        const queryParams = new URLSearchParams();
        if (filters.director.trim()) queryParams.append('director', filters.director.trim());
        if (filters.actor.trim()) queryParams.append('actor', filters.actor.trim());
        if (filters.genre.trim()) queryParams.append('genre', filters.genre.trim());

        const url = `http://127.0.0.1:5000/movies${queryParams.toString() ? `?${queryParams}` : ''}`;
        console.log("Fetching:", url);

        const res = await axios.get(url);
        setMovies(Array.isArray(res.data) ? res.data : []);
        setError(res.data.message || '');
      } catch (err) {
        console.error("Failed to fetch:", err);
        setError('Failed to fetch movies.');
        setMovies([]);
      } finally {
        setLoading(false);
      }
    }, 500),
    [] 
  );

  useEffect(() => {
    fetchMovies(filters);
  }, [filters, fetchMovies]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFilters((prev) => ({ ...prev, [name]: value }));
  };

  return (
    <div className="container-fluid mt-4 ">
      <h2 className="mb-3">Movie Explorer - Browse movies and view details about your favourite actor and director</h2>

      <div className="row mb-4">
        {['director', 'actor', 'genre'].map((filter) => (
          <div className="col-md-4" key={filter}>
            <input
              name={filter}
              value={filters[filter]}
              onChange={handleChange}
              className="form-control"
              placeholder={`Search by ${filter.charAt(0).toUpperCase() + filter.slice(1)}`}
            />
          </div>
        ))}
      </div>

      {loading ? (
        <p>Loading movies...</p>
      ) : error ? (
        <p className="text-danger">{error}</p>
      ) : movies.length === 0 ? (
        <p>No movies found.</p>
      ) : (
        <div className="row">
          {movies.map((movie) => (
            <div className="col-md-4 mb-4" key={movie._id}>
              <div className="card h-100 bg-light">
                <div className="card-body">
                  <h5 className="card-title">{movie.title}</h5>
                  <p className="card-text">
                    <strong>Release Year:</strong> {movie.release_year || 'N/A'}<br />
                    <strong>Director:</strong>{' '}
                    {movie.director_id && movie.director_name ? (
                      <Link className="text-decoration-none" to={`/director/${movie.director_id}`}>{movie.director_name}</Link>
                    ) : 'Unknown'}
                    <br />
                    <strong>Genres:</strong> {movie.genres?.join(', ') || 'None'}<br />
                    <strong>Actors:</strong>{' '}
                    {movie.actors?.map((actor, index) => (
                      <span key={actor._id}>
                        <Link className="text-decoration-none" to={`/actor/${actor._id}`}>{actor.name}</Link>
                        {index < movie.actors.length - 1 ? ', ' : ''}
                      </span>
                    )) || 'None'}
                  </p>
                  <Link to={`/movie/${movie._id}`} className="btn btn-primary">
                    View Details
                  </Link>
                </div>
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
