import React, { useState } from 'react';

function AddRecipe() {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [categoryId, setCategoryId] = useState('');
  const [ingredients, setIngredients] = useState([{ name: '', amount: '' }]);

  const handleIngredientChange = (index, field, value) => {
    const newIngredients = [...ingredients];
    newIngredients[index][field] = value;
    setIngredients(newIngredients);
  };

  const addIngredient = () => {
    setIngredients([...ingredients, { name: '', amount: '' }]);
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    const recipeData = { name, description, category_id: categoryId, ingredients };
    
    // Send a POST request to the backend
    fetch('/api/recipes', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(recipeData),
    })
      .then(response => response.json())
      .then(data => console.log('Recipe added:', data))
      .catch(error => console.error('Error adding recipe:', error));
  };

  return (
    <div>
      <h1>Add New Recipe</h1>
      <form onSubmit={handleSubmit}>
        <label>Name:</label>
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} required />

        <label>Description:</label>
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} required />

        <label>Category:</label>
        <select onChange={(e) => setCategoryId(e.target.value)} required>
          {/* Categories should be fetched or passed as a prop */}
          <option value="">Select Category</option>
          {/* Example category options */}
          <option value="1">Breakfast</option>
          <option value="2">Lunch</option>
        </select>

        <h3>Ingredients</h3>
        {ingredients.map((ingredient, index) => (
          <div key={index}>
            <label>Ingredient Name:</label>
            <input
              type="text"
              value={ingredient.name}
              onChange={(e) => handleIngredientChange(index, 'name', e.target.value)}
              required
            />
            <label>Amount:</label>
            <input
              type="text"
              value={ingredient.amount}
              onChange={(e) => handleIngredientChange(index, 'amount', e.target.value)}
              required
            />
          </div>
        ))}

        <button type="button" onClick={addIngredient}>Add Ingredient</button>
        <button type="submit">Submit Recipe</button>
      </form>
    </div>
  );
}

export default AddRecipe;
