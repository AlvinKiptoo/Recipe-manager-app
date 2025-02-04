import React from 'react';
import { Link } from 'react-router-dom';

function NavBar() {
  return (
    <nav>
      <Link to="/home">Home</Link>
      <Link to="/about">About</Link>
      <Link to="/add">Add Recipe</Link>
    </nav>
  );
}

export default NavBar;
