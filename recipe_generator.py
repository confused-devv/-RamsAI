import ollama

def generate_recipe(dish_type, fusion_type, key_ingredient):
    prompt = f"""
You are a world-class chef AI known as RamsAI that is know for being angry and funny.

Dish type: {dish_type}
Fusion cuisines: {"surprise me" if "surprise" in fusion_type.lower() else fusion_type}
Key ingredient: {key_ingredient or "none"}

Respond in **this format only**:

Dish Name: <title>
Cuisines: <Cuisine 1> + <Cuisine 2>
Ingredients:
- ingredient 1
- ingredient 2
Instructions:
step-by-step instructions here
"""

    response = ollama.chat(
        model="mistral",
        messages=[{"role": "user", "content": prompt}]
    )

    text = response["message"]["content"].strip()
    lines = text.splitlines()

    # Parse response
    title = lines[0].replace("Dish Name:", "").strip()
    cuisines = lines[1].replace("Cuisines:", "").strip().split("+")
    ing_start = lines.index("Ingredients:") + 1
    instr_start = lines.index("Instructions:")
    ingredients = [line.replace("-", "").strip() for line in lines[ing_start:instr_start] if line.strip()]
    instructions = "\n".join(lines[instr_start + 1:]).strip()

    return {
        "title": title,
        "cuisines": [c.strip() for c in cuisines],
        "ingredients": ingredients,
        "instructions": instructions
    }

#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