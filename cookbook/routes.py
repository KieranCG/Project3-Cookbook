from flask import render_template, request, redirect, url_for
from cookbook import app, db
from cookbook.models import Category, Recipe

@app.route("/")
def home():
    return render_template("recipe.html")