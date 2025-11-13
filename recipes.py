def get_all_recipes():
    """Return a list of 20 sample recipes with structured details."""

    recipes = [
        {
            "name": "Spicy Chicken Curry",
            "ingredients": ["chicken", "onion", "tomato", "garlic", "ginger", "chili powder", "oil"],
            "steps": "Heat oil, sauté onion and garlic until golden. Add chicken, tomato, and spices. Cook until chicken is tender. Garnish with coriander and serve hot.",
            "time": 45,
            "difficulty": "Medium",
            "diet": "Non-Vegetarian",
            "nutrition": {"calories": 420, "protein": 35, "fat": 18, "carbs": 15}
        },
        {
            "name": "Paneer Butter Masala",
            "ingredients": ["paneer", "tomato", "onion", "butter", "cream", "garam masala"],
            "steps": "Blend onion and tomato into paste. Cook in butter with spices. Add paneer cubes and cream, simmer for 10 mins.",
            "time": 30,
            "difficulty": "Medium",
            "diet": "Vegetarian",
            "nutrition": {"calories": 380, "protein": 20, "fat": 25, "carbs": 12}
        },
        {
            "name": "Egg Fried Rice",
            "ingredients": ["rice", "egg", "soy sauce", "onion", "carrot", "oil"],
            "steps": "Scramble eggs in oil, add onion and carrot. Mix in cooked rice and soy sauce. Stir fry for 5 minutes.",
            "time": 20,
            "difficulty": "Easy",
            "diet": "Non-Vegetarian",
            "nutrition": {"calories": 310, "protein": 12, "fat": 10, "carbs": 40}
        },
        {
            "name": "Vegetable Pulao",
            "ingredients": ["rice", "peas", "carrot", "beans", "onion", "ghee", "spices"],
            "steps": "Fry onion in ghee, add vegetables and spices. Mix rice and cook till fluffy.",
            "time": 25,
            "difficulty": "Easy",
            "diet": "Vegetarian",
            "nutrition": {"calories": 290, "protein": 8, "fat": 9, "carbs": 45}
        },
        {
            "name": "Grilled Fish with Lemon Butter",
            "ingredients": ["fish", "butter", "lemon", "garlic", "pepper", "salt"],
            "steps": "Marinate fish with lemon, garlic, and pepper. Grill until golden. Pour melted butter before serving.",
            "time": 30,
            "difficulty": "Medium",
            "diet": "Non-Vegetarian",
            "nutrition": {"calories": 330, "protein": 34, "fat": 18, "carbs": 5}
        },
        {
            "name": "Mushroom Pasta Alfredo",
            "ingredients": ["pasta", "mushroom", "cream", "butter", "garlic", "cheese"],
            "steps": "Boil pasta, sauté mushrooms in butter, add cream and cheese, mix well and serve.",
            "time": 25,
            "difficulty": "Easy",
            "diet": "Vegetarian",
            "nutrition": {"calories": 400, "protein": 15, "fat": 22, "carbs": 35}
        },
        {
            "name": "Vegetable Stir Fry",
            "ingredients": ["broccoli", "carrot", "capsicum", "soy sauce", "oil", "garlic"],
            "steps": "Heat oil, add garlic and veggies. Stir fry with soy sauce for 5 minutes.",
            "time": 15,
            "difficulty": "Easy",
            "diet": "Vegan",
            "nutrition": {"calories": 180, "protein": 7, "fat": 6, "carbs": 20}
        },
        {
            "name": "Oats Banana Smoothie",
            "ingredients": ["oats", "banana", "milk", "honey"],
            "steps": "Blend oats, banana, milk, and honey until smooth. Serve chilled.",
            "time": 5,
            "difficulty": "Easy",
            "diet": "Vegetarian",
            "nutrition": {"calories": 210, "protein": 6, "fat": 4, "carbs": 40}
        },
        {
            "name": "Tofu Veg Stir Fry",
            "ingredients": ["tofu", "broccoli", "soy sauce", "ginger", "garlic", "carrot"],
            "steps": "Sauté tofu in oil, add veggies and soy sauce, stir fry for 5–7 mins.",
            "time": 15,
            "difficulty": "Easy",
            "diet": "Vegan",
            "nutrition": {"calories": 220, "protein": 14, "fat": 10, "carbs": 15}
        },
        {
            "name": "Chole Masala",
            "ingredients": ["chickpeas", "tomato", "onion", "garlic", "ginger", "spices"],
            "steps": "Cook onion and tomato paste, add chickpeas and spices. Simmer until thick.",
            "time": 35,
            "difficulty": "Medium",
            "diet": "Vegan",
            "nutrition": {"calories": 320, "protein": 15, "fat": 8, "carbs": 45}
        },
        {
            "name": "Pancakes with Honey",
            "ingredients": ["flour", "milk", "egg", "sugar", "butter", "honey"],
            "steps": "Mix batter, pour onto hot pan, cook both sides, and drizzle with honey.",
            "time": 20,
            "difficulty": "Easy",
            "diet": "Vegetarian",
            "nutrition": {"calories": 250, "protein": 6, "fat": 8, "carbs": 35}
        },
        {
            "name": "Egg Sandwich",
            "ingredients": ["bread", "egg", "butter", "pepper", "salt"],
            "steps": "Toast bread, cook egg, and assemble sandwich with butter.",
            "time": 10,
            "difficulty": "Easy",
            "diet": "Non-Vegetarian",
            "nutrition": {"calories": 220, "protein": 10, "fat": 9, "carbs": 25}
        },
        {
            "name": "Tomato Soup",
            "ingredients": ["tomato", "onion", "garlic", "butter", "salt", "pepper"],
            "steps": "Cook tomato and onion in butter, blend, and simmer for 5 minutes.",
            "time": 15,
            "difficulty": "Easy",
            "diet": "Vegetarian",
            "nutrition": {"calories": 120, "protein": 3, "fat": 5, "carbs": 15}
        },
        {
            "name": "Lentil Soup",
            "ingredients": ["lentils", "carrot", "onion", "garlic", "salt", "pepper"],
            "steps": "Boil lentils with vegetables and spices until soft, blend slightly and serve warm.",
            "time": 25,
            "difficulty": "Easy",
            "diet": "Vegan",
            "nutrition": {"calories": 200, "protein": 12, "fat": 4, "carbs": 25}
        },
        {
            "name": "Mango Lassi",
            "ingredients": ["mango", "yogurt", "honey", "cardamom"],
            "steps": "Blend mango, yogurt, honey, and cardamom until creamy. Serve chilled.",
            "time": 5,
            "difficulty": "Easy",
            "diet": "Vegetarian",
            "nutrition": {"calories": 180, "protein": 5, "fat": 4, "carbs": 32}
        },
        {
            "name": "Garlic Butter Shrimp",
            "ingredients": ["shrimp", "garlic", "butter", "lemon", "parsley"],
            "steps": "Cook shrimp in butter with garlic until pink. Add lemon and parsley before serving.",
            "time": 20,
            "difficulty": "Easy",
            "diet": "Non-Vegetarian",
            "nutrition": {"calories": 280, "protein": 26, "fat": 14, "carbs": 5}
        },
        {
            "name": "Chocolate Mug Cake",
            "ingredients": ["flour", "cocoa powder", "sugar", "milk", "butter"],
            "steps": "Mix all ingredients in a mug and microwave for 2 minutes.",
            "time": 5,
            "difficulty": "Easy",
            "diet": "Vegetarian",
            "nutrition": {"calories": 320, "protein": 5, "fat": 12, "carbs": 45}
        },
        {
            "name": "Fruit Salad",
            "ingredients": ["apple", "banana", "grapes", "orange", "honey"],
            "steps": "Chop all fruits, drizzle honey, and toss well.",
            "time": 5,
            "difficulty": "Easy",
            "diet": "Vegan",
            "nutrition": {"calories": 150, "protein": 2, "fat": 1, "carbs": 35}
        },
        {
            "name": "Masala Omelette",
            "ingredients": ["egg", "onion", "tomato", "chili", "salt", "oil"],
            "steps": "Beat eggs, mix with chopped vegetables, and cook in hot oil until golden.",
            "time": 10,
            "difficulty": "Easy",
            "diet": "Non-Vegetarian",
            "nutrition": {"calories": 190, "protein": 11, "fat": 14, "carbs": 3}
        },
        {
            "name": "Veg Noodles",
            "ingredients": ["noodles", "carrot", "capsicum", "soy sauce", "vinegar"],
            "steps": "Boil noodles, stir-fry veggies, add sauces, and mix everything together.",
            "time": 15,
            "difficulty": "Easy",
            "diet": "Vegan",
            "nutrition": {"calories": 270, "protein": 8, "fat": 9, "carbs": 38}
        },
    ]

    return recipes


def find_recipe_by_ingredients(ingredients):
    """Find recipes matching all provided ingredients."""
    all_recipes = get_all_recipes()
    matches = []
    for recipe in all_recipes:
        if all(i.lower() in [x.lower() for x in recipe["ingredients"]] for i in ingredients):
            matches.append(recipe)
    return matches


def filter_recipes_by_diet(recipes, diet_type):
    """Filter recipes by diet type."""
    if diet_type.lower() == "any":
        return recipes
    return [r for r in recipes if r["diet"].lower() == diet_type.lower()]
