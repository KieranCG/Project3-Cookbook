from cookbook import db

class Recipe(db.Model):
    # schema for the Recipe model
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    prep_time = db.Column(db.Integer)  # in minutes
    cook_time = db.Column(db.Integer)  # in minutes
    total_time = db.Column(db.Integer)  # in minutes
    ingredients = db.relationship("Ingredient", backref="recipe", cascade="all, delete", lazy=True)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"Recipe('{self.title}', '{self.description}', '{self.servings}', '{self.total_time}')"

class Ingredient(db.Model):
    # schema for the Ingredient model
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    quantity = db.Column(db.String(50))  # e.g., "1 cup", "2 cloves"
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipe.id", ondelete="CASCADE"), nullable=False)

    def __repr__(self):
        # __repr__ to represent itself in the form of a string
        return f"Ingredient('{self.name}', '{self.quantity}')"