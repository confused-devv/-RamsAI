import ollama

def generate_recipe(dish_type, fusion_type, key_ingredient):
    prompt = f"""
You are a fusion chef AI.

Create a unique {dish_type} using {'surprise cuisines' if 'surprise' in fusion_type.lower() else fusion_type}.
Include the ingredient: {key_ingredient if key_ingredient else 'any creative ingredients'}.

Respond in the following format:

Dish Name: <title>
Cuisines: <Cuisine 1> + <Cuisine 2>
Ingredients:
- <ingredient 1>
- <ingredient 2>
Instructions:
<step-by-step instructions>
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response['message']['content']
    lines = text.strip().splitlines()

    title = lines[0].replace("Dish Name:", "").strip()
    cuisines = lines[1].replace("Cuisines:", "").strip().split("+")
    ing_start = lines.index("Ingredients:") + 1
    instr_start = lines.index("Instructions:")
    ingredients = [line.lstrip("- ").strip() for line in lines[ing_start:instr_start]]
    instructions = "\n".join(lines[instr_start+1:]).strip()

    return {
        "title": title,
        "cuisines": [c.strip() for c in cuisines],
        "ingredients": ingredients,
        "instructions": instructions
    }
