import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';

function Home() {
  const [recipes, setRecipes] = useState([]);
  const [categories, setCategories] = useState([]);
  const [selectedCategory, setSelectedCategory] = useState('');
  const [loading, setLoading] = useState(true);
  const [loadingFiltered, setLoadingFiltered] = useState(false);

  useEffect(() => {
    // Fetch all recipes
    fetch('http://localhost:5555/recipes')
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setRecipes(data);
        } else {
          console.error('Invalid data format for recipes:', data);
        }
        setLoading(false); // Stop loading once recipes are fetched
      })
      .catch((error) => {
        console.error('Error fetching recipes:', error);
        setLoading(false); // Stop loading even if there's an error
      });

    // Fetch categories
    fetch('http://localhost:5555/categories')
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setCategories(data);
        } else {
          console.error('Invalid data format for categories:', data);
        }
      })
      .catch((error) => console.error('Error fetching categories:', error));
  }, []);

  // Handle category change for filtering
  const handleCategoryChange = (e) => {
    setSelectedCategory(e.target.value);
    setLoadingFiltered(true); // Set loading state while fetching filtered recipes
    // Fetch recipes filtered by category
    fetch(`http://localhost:5555/recipes?category=${e.target.value}`)
      .then((response) => response.json())
      .then((data) => {
        if (Array.isArray(data)) {
          setRecipes(data);
        } else {
          console.error('Invalid data format for filtered recipes:', data);
        }
        setLoadingFiltered(false); // Stop loading after data is fetched
      })
      .catch((error) => {
        console.error('Error fetching filtered recipes:', error);
        setLoadingFiltered(false); // Stop loading even if there's an error
      });
  };

  return (
    <div>
      <h1>Recipe List</h1>

      {/* Category filter dropdown */}
      <select 
        onChange={handleCategoryChange} 
        value={selectedCategory} // Set the dropdown to reflect the selected category
        style={{ marginBottom: '20px' }}
      >
        <option value="">All Categories</option>
        {categories.map((category) => (
          <option key={category.id} value={category.id}>
            {category.name}
          </option>
        ))}
      </select>

      {/* Loading state for recipes */}
      {loading ? (
        <p>Loading...</p>
      ) : (
        <div>
          {/* Loading state for filtered recipes */}
          {loadingFiltered ? (
            <p>Loading filtered recipes...</p>
          ) : (
            <ul>
              {recipes.map((recipe) => (
                <li key={recipe.id}>
                  <Link to={`/recipe/${recipe.id}`}>{recipe.name}</Link>
                </li>
              ))}
            </ul>
          )}
        </div>
      )}

      {/* Link to add new recipe */}
      <Link to="/add">Add New Recipe</Link>
    </div>
  );
}

export default Home;
