from flask_restful import Resource, Api
from flask import request, jsonify
from config import app, db
from models import Recipe, Category, Ingredient, FavoriteRecipes

# Initialize the API
api = Api(app)

class RecipeResource(Resource):
    def get(self, id=None):
        if id:
            recipe = Recipe.query.get(id)
            if not recipe:
                return {"error": "Recipe not found"}, 404
            return recipe.to_dict()
        recipes = Recipe.query.all()
        return jsonify([recipe.to_dict() for recipe in recipes])

    def post(self):
        data = request.get_json()
        new_recipe = Recipe(
            name=data['name'], 
            description=data['description'],
            category_id=data['category_id']
        )
        db.session.add(new_recipe)
        db.session.commit()
        return jsonify(new_recipe.to_dict()), 201

    def put(self, id):
        recipe = Recipe.query.get(id)
        if not recipe:
            return {"error": "Recipe not found"}, 404
        data = request.get_json()
        recipe.name = data.get('name', recipe.name)
        recipe.description = data.get('description', recipe.description)
        recipe.category_id = data.get('category_id', recipe.category_id)
        db.session.commit()
        return jsonify(recipe.to_dict())

    def delete(self, id):
        recipe = Recipe.query.get(id)
        if not recipe:
            return {"error": "Recipe not found"}, 404
        db.session.delete(recipe)
        db.session.commit()
        return '', 204

# Register Resources with API
api.add_resource(RecipeResource, '/recipes', '/recipes/<int:id>')

class CategoryResource(Resource):
    def get(self):
        categories = Category.query.all()
        return jsonify([category.to_dict() for category in categories])

    def post(self):
        data = request.get_json()
        new_category = Category(name=data['name'])
        db.session.add(new_category)
        db.session.commit()
        return jsonify(new_category.to_dict()), 201

api.add_resource(CategoryResource, '/categories')

class IngredientResource(Resource):
    def get(self):
        ingredients = Ingredient.query.all()
        return jsonify([ingredient.to_dict() for ingredient in ingredients])

    def post(self):
        data = request.get_json()
        new_ingredient = Ingredient(
            name=data['name'],
            amount=data['amount'],
            recipe_id=data['recipe_id']
        )
        db.session.add(new_ingredient)
        db.session.commit()
        return jsonify(new_ingredient.to_dict()), 201

api.add_resource(IngredientResource, '/ingredients')

class FavoriteRecipesResource(Resource):
    def post(self):
        data = request.get_json()
        new_favorite = FavoriteRecipes(
            user_id=data['user_id'],
            recipe_id=data['recipe_id'],
            comment=data.get('comment')
        )
        db.session.add(new_favorite)
        db.session.commit()
        return jsonify(new_favorite.to_dict()), 201

api.add_resource(FavoriteRecipesResource, '/favorite-recipes')

# Error handling route not found
@app.errorhandler(404)
def page_not_found(e):
    return jsonify(error="Not found"), 404

if __name__ == '__main__':
    app.run(port=5555, debug=True)
