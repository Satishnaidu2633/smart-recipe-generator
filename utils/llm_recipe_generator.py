import random

def generate_recipes(ingredients, diet):
    """
    Highly dynamic offline recipe generator.
    Each recipe is generated independently with unique step structure, cooking verbs, and style.
    """

    if not ingredients:
        ingredients = ["salt", "water"]

    main = ingredients[0].lower()

    cuisines = ["Indian", "Italian", "Asian", "Mexican", "Mediterranean"]
    adjectives = ["Spicy", "Tasty", "Homemade", "Delicious", "Quick", "Savory", "Crispy", "Healthy"]
    methods = ["Fried", "Grilled", "Curried", "Baked", "Roasted", "Sauteed", "Stir-Fried"]

    # Common cooking verbs
    verbs = [
        "chop", "slice", "marinate", "fry", "sauté", "bake", "grill", "boil", "mix", "toss", "season", "roast"
    ]

    # Garnish ideas
    garnishes = [
        "fresh coriander", "lemon juice", "grated cheese", "spring onions", "olive oil drizzle",
        "chili flakes", "fresh herbs", "mint leaves"
    ]

    def create_steps(main, cuisine, method, ingredients):
        """
        Generate natural cooking instructions using variety and randomness.
        """
        intro = [
            f"Prepare all ingredients: {', '.join(ingredients)}.",
            f"Gather the ingredients like {', '.join(ingredients)} and get ready to cook.",
            f"Keep all your ingredients such as {', '.join(ingredients)} on the counter."
        ]
        cook_start = [
            f"Heat some oil or butter in a pan and {random.choice(verbs)} {random.choice(ingredients)}.",
            f"In a skillet, start by {random.choice(verbs)}ing {random.choice(ingredients)} until aromatic.",
            f"Warm up oil and gently {random.choice(verbs)} the {main} with spices."
        ]
        mid = [
            f"Add remaining ingredients and cook until the {main} turns golden brown.",
            f"Mix in the rest of the ingredients and let them simmer together.",
            f"Add spices, salt, and herbs, stirring for 5–10 minutes until thick and flavorful."
        ]
        finish = [
            f"Garnish with {random.choice(garnishes)} before serving.",
            f"Top it off with {random.choice(garnishes)} for a tasty finish.",
            f"Serve hot with rice, bread, or salad, and a hint of {random.choice(garnishes)}."
        ]

        steps = [random.choice(intro), random.choice(cook_start), random.choice(mid), random.choice(finish)]
        numbered = [f"{i+1}. {s}" for i, s in enumerate(steps)]
        return " ".join(numbered)

    def make_recipe():
        cuisine = random.choice(cuisines)
        adj = random.choice(adjectives)
        method = random.choice(methods)

        recipe_name = f"{adj} {cuisine} {main.title()} {method}"

        instructions = create_steps(main, cuisine, method, ingredients)

        # Realistic nutritional info
        nutrition = {
            "calories": random.randint(280, 550),
            "protein": random.randint(10, 40),
            "fat": random.randint(8, 25),
            "carbs": random.randint(10, 45)
        }

        return {
            "name": recipe_name,
            "ingredients": ingredients,
            "instructions": instructions,
            "nutrition": nutrition
        }

    # Generate 2–3 distinct recipes
    num_recipes = random.randint(2, 3)
    recipes = [make_recipe() for _ in range(num_recipes)]
    return recipes
