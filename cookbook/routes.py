from flask import render_template, request, redirect, url_for, flash
from cookbook import app, db
from cookbook.models import Category, Recipe

@app.route("/")
def home():
    return render_template("recipe.html")

@app.route("/categories")
def categories():
    return render_template("categories.html")


@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        try:
            category_name = request.form.get("category_name")
            if not category_name:
                raise ValueError("Category name is required.")
            
            category = Category(category_name=category_name)
            db.session.add(category)
            db.session.commit()
            flash("Category added successfully.", "success")
            return redirect(url_for("categories"))
        except Exception as e:
            flash(f"Error occurred: {str(e)}", "error")
            db.session.rollback()  # Rollback the session to prevent partial changes
    return render_template("add_category.html")