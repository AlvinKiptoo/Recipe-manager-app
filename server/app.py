#!/usr/bin/env python3

# Standard library imports
from flask import request, jsonify
from flask_restful import Resource, Api

# Remote library imports
from config import app, db

# Local imports
# Add your model imports here
from models import Recipe, Category, Ingredient, FavoriteRecipes, User


# Initialize the API
api = Api(app)

# Views go here!

# Basic route to test the server
@app.route('/')
def index():
    return '<h1>Recipe Manager API</h1>'

# CRUD Routes for Recipes

@app.route('/recipes', methods=['GET', 'POST'])
def manage_recipes():
    if request.method == 'GET':
        recipes = Recipe.query.all()
        return jsonify([recipe.to_dict() for recipe in recipes])  # Assuming `to_dict()` method exists on your models
    
    if request.method == 'POST':
        data = request.get_json()
        new_recipe = Recipe(
            name=data['name'], 
            description=data['description'],
            category_id=data['category_id']
        )
        db.session.add(new_recipe)
        db.session.commit()
        return jsonify(new_recipe.to_dict()), 201


@app.route('/recipes/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def recipe_detail(id):
    recipe = Recipe.query.get(id)
    
    if not recipe:
        return jsonify({"error": "Recipe not found"}), 404

    if request.method == 'GET':
        return jsonify(recipe.to_dict())
    
    if request.method == 'PUT':
        data = request.get_json()
        recipe.name = data.get('name', recipe.name)
        recipe.description = data.get('description', recipe.description)
        recipe.category_id = data.get('category_id', recipe.category_id)
        db.session.commit()
        return jsonify(recipe.to_dict())
    
    if request.method == 'DELETE':
        db.session.delete(recipe)
        db.session.commit()
        return '', 204

# CRUD Routes for Categories (optional)

@app.route('/categories', methods=['GET', 'POST'])
def manage_categories():
    if request.method == 'GET':
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories])
    
    if request.method == 'POST':
        data = request.get_json()
        new_category = Category(name=data['name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify(new_category.to_dict()), 201


# CRUD Routes for Ingredients (optional)

@app.route('/ingredients', methods=['GET', 'POST'])
def manage_ingredients():
    if request.method == 'GET':
        ingredients = Ingredient.query.all()
        return jsonify([ingredient.to_dict() for ingredient in ingredients])
    
    if request.method == 'POST':
        data = request.get_json()
        new_ingredient = Ingredient(
            name=data['name'],
            amount=data['amount'],
            recipe_id=data['recipe_id']
        )
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify(new_ingredient.to_dict()), 201


# User and FavoriteRecipes routes (optional)
@app.route('/favorite-recipes', methods=['POST'])
def add_to_favorites():
    data = request.get_json()
    new_favorite = FavoriteRecipes(
        user_id=data['user_id'],
        recipe_id=data['recipe_id'],
        comment=data.get('comment')
    )
    db.session.add(new_favorite)
    db.session.commit()
    return jsonify(new_favorite.to_dict()), 201

# Error handling route not found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not found"), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)

