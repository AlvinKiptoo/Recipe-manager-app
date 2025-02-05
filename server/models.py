from datetime import datetime
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.ext.associationproxy import association_proxy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()

# Define the Recipe model
class Recipe(db.Model, SerializerMixin):
    __tablename__ = 'recipes'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationship with Category
    category = db.relationship('Category', backref='recipes', lazy=True)
    # Relationship with Ingredients
    ingredients = db.relationship('Ingredient', backref='recipe', lazy=True)
    # Relationship with FavoriteRecipes (Many-to-Many)
    favorites = db.relationship('FavoriteRecipes', back_populates='recipe', lazy=True)

    # Association Proxy for ingredients' names
    ingredient_names = association_proxy('ingredients', 'name')

    # Method to convert to dictionary for JSON response
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category_id': self.category_id,
            'category': self.category.to_dict() if self.category else None,
            'ingredients': [ingredient.to_dict() for ingredient in self.ingredients],
            'created_at': self.created_at,
        }

# Define the Category model
class Category(db.Model, SerializerMixin):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    # Method to convert to dictionary for JSON response
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
        }

# Define the Ingredient model
class Ingredient(db.Model, SerializerMixin):
    __tablename__ = 'ingredients'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    amount = db.Column(db.String(100), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)

    # Method to convert to dictionary for JSON response
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'amount': self.amount,
            'recipe_id': self.recipe_id,
        }

# Define the User model (for user-related functionality)
class User(db.Model, SerializerMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)

    # Method to convert to dictionary for JSON response
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
        }

# Define the FavoriteRecipes model (Many-to-Many relationship with additional attributes)
class FavoriteRecipes(db.Model, SerializerMixin):
    __tablename__ = 'favorite_recipes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.id'), nullable=False)
    comment = db.Column(db.String(500), nullable=True)

    # Relationship with User and Recipe
    user = db.relationship('User', backref='favorites', lazy=True)
    recipe = db.relationship('Recipe', back_populates='favorites')

    # Method to convert to dictionary for JSON response
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'recipe_id': self.recipe_id,
            'comment': self.comment,
            'user': self.user.to_dict(),
            'recipe': self.recipe.to_dict(),
        }

# Models go here!
