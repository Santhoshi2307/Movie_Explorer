import { Link } from 'react-router-dom';

export default function Navbar() {
  return (
    <nav className="navbar navbar-dark bg-dark navbar-expand-lg">
      <div className="container-fluid">
        <Link className="navbar-brand" to="/" onClick={() => window.location.href = '/'}>Movie Explorer</Link>
      </div>
    </nav>
  );
}