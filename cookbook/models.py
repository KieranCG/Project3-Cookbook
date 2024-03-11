from cookbook import db

class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    cook_time = db.Column(db.Integer)  # in minutes
    ingredients = db.relationship("Ingredient", backref="recipe", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"Recipe('{self.recipe_name}', '{self.servings}', '{self.total_time}')"

class Ingredient(db.Model):
    # schema for the Ingredient model
    id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(50))  # e.g., "1 cup", "2 cloves"
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"Ingredient('{self.ingredient_name}', '{self.quantity}')"