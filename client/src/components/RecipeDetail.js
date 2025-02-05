import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function RecipeDetail() {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Fetch the specific recipe by ID
    fetch(`http://localhost:5555/recipes/${id}`)
      .then(response => response.json())
      .then(data => {
        setRecipe(data);
        setLoading(false);
      })
      .catch(error => {
        console.error('Error fetching recipe details:', error);
        setLoading(false);
      });
  }, [id]);

  if (loading) return <div>Loading...</div>;
  if (!recipe) return <div>Error: Recipe not found</div>;

  // Safe checks
  const categoryName = recipe.category ? recipe.category.name : "Unknown";
  const ingredients = Array.isArray(recipe.ingredients) ? recipe.ingredients : [];

  return (
    <div>
      <h1>{recipe.name}</h1>
      <p>{recipe.description}</p>
      <h3>Category: {categoryName}</h3>
      <h4>Ingredients</h4>
      <ul>
        {ingredients.length > 0 ? (
          ingredients.map(ingredient => (
            <li key={ingredient.id}>{ingredient.name}: {ingredient.amount}</li>
          ))
        ) : (
          <li>No ingredients listed</li>
        )}
      </ul>
    </div>
  );
}

export default RecipeDetail;
