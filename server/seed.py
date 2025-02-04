#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Remote library imports
from faker import Faker

# Local imports
from app import app
from models import db, Recipe, Category, Ingredient, User, FavoriteRecipes

if __name__ == '__main__':
    fake = Faker()
    with app.app_context():
        print("Starting seed...")

        # Clear existing data in tables (Optional: useful for a fresh start)
        db.drop_all()
        db.create_all()

        # Seed Categories
        categories = ['Dessert', 'Main Course', 'Appetizer', 'Side Dish', 'Beverage']
        for category_name in categories:
            category = Category(name=category_name)
            db.session.add(category)

        # Commit category additions
        db.session.commit()

        # Seed Users
        users = []
        for _ in range(10):
            user = User(username=fake.user_name(), email=fake.email())
            users.append(user)
        db.session.add_all(users)

        # Commit user additions
        db.session.commit()

        # Seed Recipes and Ingredients
        for _ in range(20):
            recipe_name = fake.sentence(nb_words=3)
            category = rc(Category.query.all())  # Randomly pick a category
            recipe = Recipe(name=recipe_name, description=fake.text(), category_id=category.id)
            db.session.add(recipe)

            # Seed Ingredients for each Recipe
            for _ in range(randint(3, 7)):  # Each recipe will have 3-7 ingredients
                ingredient = Ingredient(name=fake.word(), amount=fake.random_int(min=1, max=5), recipe_id=recipe.id)
                db.session.add(ingredient)

        # Commit recipe and ingredient additions
        db.session.commit()

        # Seed FavoriteRecipes (many-to-many relationship with additional comment)
        for user in users:
            for _ in range(randint(1, 5)):  # Each user can have 1 to 5 favorite recipes
                recipe = rc(Recipe.query.all())  # Randomly pick a recipe
                comment = fake.sentence()
                favorite_recipe = FavoriteRecipes(user_id=user.id, recipe_id=recipe.id, comment=comment)
                db.session.add(favorite_recipe)

        # Commit favorite recipes additions
        db.session.commit()

        print("Seeding complete!")
