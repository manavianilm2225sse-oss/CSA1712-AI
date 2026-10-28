
# Diet Suggestion System

diets = {
    "diabetes": "Whole grains, vegetables, and low-sugar foods",
    "obesity": "Vegetables, fruits, and portion-controlled meals",
    "anemia": "Iron-rich foods like spinach, beans, and lentils",
    "hypertension": "Low-salt foods, fruits, and vegetables"
}

disease = input("Enter disease: ").lower()

if disease in diets:
    print("Suggested Diet:", diets[disease])
else:
    print("No diet suggestion available")

