# 🍳 Smart Recipe Generator

The Smart Recipe Generator is an AI-assisted recipe recommendation system built using Streamlit.
Users can provide ingredients through text or image upload, and the system generates recipes using a combination of rule-based matching and AI-powered fallback generation.

### 🚀 Features
🔍 Ingredient Input

Text Input – Enter ingredients comma-separated

Image Upload – Automatically recognize ingredients from an image (optional)

### 🍽️ Recipe Generation

Rule-Based Matching
Matches your ingredients with a local list of curated recipes.

AI Fallback Recipes
If no direct match is found, an open-source LLM generates recipes with:

Step-by-step instructions

Ingredients

Nutrition details (Calories, Protein, Fat, Carbs)

### ✨ Additional Features

Streaming typing effect for instructions

Dietary filters (Vegetarian, Vegan, Non-Vegetarian)

Difficulty filter

Cooking time filter

Clean and responsive UI

### 📁 Project Structure
Smart-Recipe-Generator/
│── app.py
│── recipes.py
│── requirements.txt
│
└── utils/
    ├── ingredient_recognition.py
    ├── llm_recipe_generator.py

### 🔧 Installation
1️⃣ Clone the repository

`
git clone https://github.com/your-username/smart-recipe-generator.git
cd smart-recipe-generator`

2️⃣ Create & activate virtual environment (optional)

`
python -m venv .venv

`
.venv\Scripts\activate`

3️⃣ Install dependencies

`
pip install -r requirements.txt`

▶️ Running the App
Start the Streamlit app:

`
streamlit run app.py`


The application will launch in your browser at:

http://localhost:8501

### 🧠 How It Works
➤ Rule-Based Engine

Matches ingredients against a predefined recipe dataset (recipes.py).

➤ AI Fallback Engine

Uses an open-source LLM to generate fully structured recipes with nutritional data if no rule-based match is found.

➤ Image Ingredient Recognition

Detects ingredients from photos using a lightweight computer vision model.

### 🤝 Contributing

Contributions are welcome!
Feel free to open issues or submit pull requests.

### 📜 License

This project is open-source under the MIT License.

### 👨‍🍳 Developed By

Vulli Satish Naidu
