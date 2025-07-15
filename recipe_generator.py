import ollama

def generate_recipe(dish_type, fusion_type, key_ingredient):
    prompt = f"""
You are a fusion chef AI.

Create a unique {dish_type} using {'surprise cuisines' if 'surprise' in fusion_type.lower() else fusion_type}.
Include the ingredient: {key_ingredient if key_ingredient else 'any creative ingredients'}.

Respond in the following format:
oh my fucking god all i want you to do is give me an ingredient list is that so hard for you to fucking do
Dish Name: <title>
Cuisines: <Cuisine 1> + <Cuisine 2>
Ingredients:
- <ingredient 1>
- <ingredient 2>
Instructions:
<step-by-step instructions>
"""

    response = ollama.chat(model="mistral", messages=[
        {"role": "user", "content": prompt}
    ])

    return {
        "title": "Fusion Dish",
        "cuisines": [],
        "ingredients": [],
        "instructions": response['message']['content'].strip()
    }
