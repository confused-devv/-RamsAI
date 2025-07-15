from recipe_generator import generate_recipe
from novelty_guard import is_novel, add_to_index

if __name__ == "__main__":
    print("👨‍🍳 Welcome to RamsAI!")

    dish_type = input("🍽️ What kind of dish would you like? (e.g., dessert, main course, snack): ")
    fusion_type = input("🌏 What two cuisines should be fused? (e.g., Indian + Japanese or 'surprise me'): ")
    key_ingredient = input("🧂 Any specific ingredient you'd like included? (or press Enter to skip): ")

    for attempt in range(5):
        recipe = generate_recipe(dish_type, fusion_type, key_ingredient)

        # Reconstruct full recipe text for novelty checking
        full_text = f"""
        Dish Name: {recipe['title']}
        Cuisines: {' + '.join(recipe['cuisines'])}

        Ingredients:
        {chr(10).join(f'- {item}' for item in recipe['ingredients'])}

        Instructions:
        {recipe['instructions']}
        """.strip()

        if is_novel(full_text):
            print("✅ Novel recipe accepted!\n")
            add_to_index(full_text)

            print(f"🍽️ Dish Name: {recipe['title']}")
            print(f"🌏 Cuisines: {', '.join(recipe['cuisines'])}\n")

            print("🧂 Ingredients:")
            for item in recipe['ingredients']:
                print(f"  • {item}")


            break
        else:
            print("⚠️ Recipe too similar, retrying...\n")
    else:
        print("❌ Couldn't generate a novel recipe in 5 tries.")



from image_generator import generate_image

# Generate a smart image prompt
image_prompt = f"{recipe['title']} — A {dish_type} combining {fusion_type}. {recipe['instructions'].splitlines()[0]}"

img_path = generate_image(image_prompt, output_path="static/dish.png")
