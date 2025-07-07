import { Routes, Route } from 'react-router-dom';
import MovieList from './pages/MovieList';
import MovieDetail from './pages/MovieDetail';
import ActorProfile from './pages/ActorProfile';
import DirectorProfile from './pages/DirectorProfile';
import Navbar from './components/Navbar';



export default function App() {
  return (
    <>
      <Navbar />
      <Routes>
        <Route path="/" element={<MovieList />} />
        <Route path="/movie/:id" element={<MovieDetail />} />
        <Route path="/actor/:id" element={<ActorProfile />} />
        <Route path="/director/:id" element={<DirectorProfile />} />
      </Routes>
    </>
  );
}