def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal Weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def build_prompt(name, gender, height, weight, goal, fitness_level, equipment):

    bmi = calculate_bmi(weight, height)
    bmi_status = bmi_category(bmi)

    equipment_list = ", ".join(equipment) if equipment else "No Equipment"

    prompt = f"""
You are a certified professional fitness trainer.
IMPORTANT:
- Do NOT write introduction.
- Do NOT write explanation.
- Do NOT give nutrition advice.
- Output ONLY the workout plan.
- Keep it concise.
User Profile:
Name: {name}
Gender: {gender}
Height: {height} cm
Weight: {weight} kg
BMI: {bmi:.2f} ({bmi_status})
Goal: {goal}
Fitness Level: {fitness_level}
Available Equipment: {equipment_list}
STRICT FORMAT:
Day 1:
Warm-up:
Main Workout (sets x reps):
Rest:
Cooldown:
Day 2:
Warm-up:
Main Workout (sets x reps):
Rest:
Cooldown:
Day 3:
Warm-up:
Main Workout (sets x reps):
Rest:
Cooldown:
Day 4:
Warm-up:
Main Workout (sets x reps):
Rest:
Cooldown:
Day 5:
Warm-up:
Main Workout (sets x reps):
Rest:
Cooldown:
Each day must contain at least 4 exercises.
Limit each day to maximum 5 exercises.
Keep total response under 900 words.
"""

    return prompt, bmi, bmi_status
