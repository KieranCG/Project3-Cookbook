from flask import render_template, request, redirect, url_for
from cookbook import app, db
from cookbook.models import Category, Recipe


@app.route("/")
def home():
    try:
        recipes = Recipe.query.order_by(Recipe.id).all()
        print(recipes)  # Print recipes to verify if they are fetched correctly
        categories = Category.query.order_by(Category.category_name).all()  # Fetch categories as well
        return render_template("recipe.html", recipes=recipes, categories=categories)
    except Exception as e:
        print(f"Error fetching recipes: {str(e)}")  # Log error message
        return "Error fetching recipes. Please try again later.", 500


@app.route("/categories")
def categories():
    categories = list(Category.query.order_by(Category.category_name).all())
    return render_template("categories.html", categories=categories)


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = Category(category_name=request.form.get("category_name"))
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("add_category.html")

@app.route("/edit_category/<int:category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    category = Category.query.get_or_404(category_id)
    if request.method == "POST":
        category.category_name = request.form.get("category_name")
        db.session.commit()
        return redirect(url_for("categories"))
    return render_template("edit_category.html", category=category)

@app.route("/delete_category/<int:category_id>")
def delete_category(category_id):
    category = Category.query.get_or_404(category_id)
    db.session.delete(category)
    db.session.commit()
    return redirect(url_for("categories"))

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        try:
            recipe = Recipe(
                recipe_name=request.form.get("recipe_name"),
                description=request.form.get("description"),
                instructions=request.form.get("instructions"),
                servings=request.form.get("servings"),
                prep_time=request.form.get("prep_time"),
                cook_time=request.form.get("cook_time"),
                total_time=request.form.get("total_time"),
                category_id=request.form.get("category_id")
            )
            db.session.add(recipe)
            db.session.commit()
            print("Recipe added successfully.")  # Log success message
            return redirect(url_for("home"))
        except Exception as e:
            print(f"Error adding recipe: {str(e)}")  # Log error message
            db.session.rollback()  # Rollback transaction in case of error
    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<int:recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    categories = list(Category.query.order_by(Category.category_name).all())
    if request.method == "POST":
        recipe.recipe_name = request.form.get("recipe_name")
        recipe.description = request.form.get("description")
        recipe.instructions = request.form.get("instructions")
        recipe.servings = request.form.get("servings")
        recipe.prep_time = request.form.get("prep_time")
        recipe.cook_time = request.form.get("cook_time")
        recipe.total_time = request.form.get("total_time")
        recipe.category_id = request.form.get("category_id")
        db.session.commit()
    return render_template("edit_recipe.html", recipe=recipe, categories=categories)

@app.route("/delete_recipe/<int:recipe_id>")
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for("home"))  # Redirect to home page after deleting