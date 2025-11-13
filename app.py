import streamlit as st
import time
from PIL import Image

# Import utilities
from utils.ingredient_recognition import recognize_ingredients
from utils.llm_recipe_generator import generate_recipes
from recipes import get_all_recipes, find_recipe_by_ingredients, filter_recipes_by_diet

# --- Streamlit App Configuration ---
st.set_page_config(page_title="Smart Recipe Generator", page_icon="🍳", layout="wide")
st.title("🍽️ Smart Recipe Generator")
st.markdown("Generate delicious recipes using the ingredients you have!")

# --- Ingredient Input Section ---
option = st.radio("Choose Input Type:", ["Text Input", "Upload Image"])
ingredients = []

if option == "Text Input":
    user_input = st.text_area("Enter ingredients (comma separated):", placeholder="e.g., tomato, onion, cheese")
    if user_input:
        ingredients = [i.strip().lower() for i in user_input.split(",")]

elif option == "Upload Image":
    uploaded_file = st.file_uploader("Upload an image of your ingredients", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_column_width=True)
        with st.spinner("Recognizing ingredients..."):
            ingredients = recognize_ingredients(image)
        st.success(f"Detected Ingredients: {', '.join(ingredients)}")

# --- Sidebar Preferences ---
st.sidebar.header("Filters & Preferences")
diet = st.sidebar.selectbox("Dietary Preference", ["Any", "Vegetarian", "Vegan", "Non-Vegetarian"])
difficulty = st.sidebar.selectbox("Difficulty", ["Any", "Easy", "Medium", "Hard"])
max_time = st.sidebar.slider("Max Cooking Time (minutes)", 10, 120, 60)
servings = st.sidebar.slider("Servings", 1, 6, 2)

# --- Load Local Recipes (20 Recipes) ---
all_recipes = get_all_recipes()

# Helper function to simulate typing animation
def stream_text(text, delay=0.02):
    """Displays text character by character for a streaming effect."""
    placeholder = st.empty()
    full_text = ""
    for char in text:
        full_text += char
        placeholder.markdown(full_text)
        time.sleep(delay)

# --- Recipe Generation Logic ---
if st.button("Generate Recipes 🍲"):
    if ingredients:
        st.info("Finding best matches for your ingredients...")

        # Match recipes from local dataset
        matched_recipes = find_recipe_by_ingredients(ingredients)

        # Apply filters
        filtered_recipes = [
            r for r in matched_recipes
            if (diet == "Any" or r["diet"].lower() == diet.lower())
            and (difficulty == "Any" or r["difficulty"].lower() == difficulty.lower())
            and (r["time"] <= max_time)
        ]

        # --- Display Matching Recipes ---
        if filtered_recipes:
            st.success(f"Found {len(filtered_recipes)} matching recipes!")
            for r in filtered_recipes[:5]:
                st.subheader(f"🍴 {r['name']}")
                st.write(f"⏱️ {r['time']} mins | 🧑‍🍳 {r['difficulty']} | 🥗 {r['diet']}")
                st.markdown("**Ingredients:** " + ", ".join(r["ingredients"]))

                st.markdown("**Instructions:**")
                stream_text(r["steps"], delay=0.015)  # 

                st.markdown(
                    f"**Nutrition (approx):** {r['nutrition']['calories']} kcal | Protein: {r['nutrition']['protein']}g | "
                    f"Fat: {r['nutrition']['fat']}g | Carbs: {r['nutrition']['carbs']}g"
                )
                st.markdown("---")

        # --- Fall Back to AI Rule-Based Generator ---
        else:
            st.warning("Generating new recipe ideas for you...")
            ai_recipes = generate_recipes(ingredients, diet)
            for recipe in ai_recipes:
                st.subheader(f"🍲 {recipe['name']}")
                st.write("**Ingredients:**", ", ".join(recipe["ingredients"]))

                st.markdown("**Instructions:**")
                stream_text(recipe["instructions"], delay=0.015)

                st.markdown(
                    f"**Nutrition (approx):** {recipe['nutrition']['calories']} kcal | "
                    f"Protein: {recipe['nutrition']['protein']}g | "
                    f"Fat: {recipe['nutrition']['fat']}g | "
                    f"Carbs: {recipe['nutrition']['carbs']}g"
                )
                st.markdown("---")

    else:
        st.error("Please enter or upload ingredients first!")

# --- Feedback Section ---
st.sidebar.header("Feedback")
rating = st.sidebar.slider("Rate this app", 1, 5, 3)
if st.sidebar.button("Submit Rating"):
    st.sidebar.success("Thank you for your feedback! 🙌")

st.sidebar.markdown("---")
st.sidebar.markdown("**Developed by Satish Naidu** 👨‍🍳")
