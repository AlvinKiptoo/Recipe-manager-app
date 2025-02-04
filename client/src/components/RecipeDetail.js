import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';

function RecipeDetail() {
  const { id } = useParams();
  const [recipe, setRecipe] = useState(null);

  useEffect(() => {
    // Fetch the specific recipe by ID
    fetch(`/api/recipes/${id}`)
      .then(response => response.json())
      .then(data => setRecipe(data))
      .catch(error => console.error('Error fetching recipe details:', error));
  }, [id]);

  if (!recipe) return <div>Loading...</div>;

  return (
    <div>
      <h1>{recipe.name}</h1>
      <p>{recipe.description}</p>
      <h3>Category: {recipe.category.name}</h3>
      <h4>Ingredients</h4>
      <ul>
        {recipe.ingredients.map(ingredient => (
          <li key={ingredient.id}>{ingredient.name}: {ingredient.amount}</li>
        ))}
      </ul>
    </div>
  );
}

export default RecipeDetail;
