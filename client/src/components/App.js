import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Home from './Home';
import RecipeDetail from './RecipeDetail';
import AddRecipe from './AddRecipe';
import NavBar from './NavBar';

function App() {
  return (
    <Router>
      <NavBar />
      <Switch>
        <Route path="/home" component={Home} />
        <Route path="/" exact component={Home} />
        <Route path="/recipe/:id" component={RecipeDetail} />
        <Route path="/add" component={AddRecipe} />
      </Switch>
    </Router>
  );
}

export default App;
