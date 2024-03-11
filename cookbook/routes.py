from flask import render_template, request, redirect, url_for
from cookbook import app, db
from cookbook.models import Recipe, Ingredient

@app.route("/")
def home():
    return render_template("recipe.html")

@app.route("/recipe")
def recipe():
    return render_template("recipe.html")

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        try:
            # Retrieve data from the form submission
            title = request.form.get("title")
            description = request.form.get("description")
            instructions = request.form.get("instructions")
            servings = int(request.form.get("servings"))
            prep_time = int(request.form.get("prep_time"))
            cook_time = int(request.form.get("cook_time"))
            total_time = int(request.form.get("total_time"))
            
            # Validate form data
            if not all([title, description, instructions]):
                raise ValueError("Title, description, and instructions are required.")
            if servings < 1:
                raise ValueError("Servings must be a positive integer.")
            if prep_time < 0 or cook_time < 0 or total_time < 0:
                raise ValueError("Prep time, cook time, and total time must be non-negative integers.")
            
            # Create a new Recipe instance with the retrieved data
            new_recipe = Recipe(
                title=title,
                description=description,
                instructions=instructions,
                servings=servings,
                prep_time=prep_time,
                cook_time=cook_time,
                total_time=total_time
            )

            # Add the new recipe to the database session
            db.session.add(new_recipe)
            db.session.commit()

            # Redirect to the recipe page
            return redirect(url_for("recipe"))
        except ValueError as e:
            # Handle validation errors
            error_message = str(e)
            return render_template("add_recipe.html", error_message=error_message)
        except Exception as e:
            # Handle unexpected errors
            error_message = "An error occurred while processing your request."
            return render_template("add_recipe.html", error_message=error_message)
    else:
        # Handle GET request (render form template)
        return render_template("add_recipe.html")