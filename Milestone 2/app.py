import streamlit as st
from huggingface_hub import InferenceClient
import os

# -------------------------
# PAGE CONFIG
# -------------------------
st.set_page_config(page_title="FitPlan-AI", page_icon="💪")
st.title("💪 FitPlan-AI: Personalized Fitness Profile")

# -------------------------
# SESSION STATE FOR PAGE NAVIGATION
# -------------------------
if "page" not in st.session_state:
    st.session_state.page = "form"

# -------------------------
# LOAD HF CLIENT (CACHED)
# -------------------------
@st.cache_resource
def get_hf_client():
    hf_token = os.getenv("HF_TOKEN")

    if not hf_token:
        raise ValueError("HF_TOKEN not set in environment variables.")

    return InferenceClient(
        model="mistralai/Mistral-7B-Instruct-v0.2",
        token=hf_token
    )

# -------------------------
# BMI FUNCTIONS
# -------------------------
def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100
    return round(weight / (height_m ** 2), 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 24.9:
        return "Normal"
    elif bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# -------------------------
# PROMPT BUILDER (AGE ADDED)
# -------------------------
def build_prompt(name, age, height, weight, goal, level, equipment, bmi, bmi_status):
    equipment_list = ", ".join(equipment)

    prompt = f"""
You are a certified professional fitness trainer.
IMPORTANT:
- Do NOT write introduction.
- Do NOT write explanation.
- Do NOT give nutrition advice.
- Output ONLY the workout plan.
- Keep it concise.
Client Details:
Name: {name}
Age: {age}
Height: {height} cm
Weight: {weight} kg
BMI: {bmi} ({bmi_status})
Goal: {goal}
Fitness Level: {level}
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
Each day must contain 4–5 exercises only.
Keep total response under 900 words.
"""
    return prompt.strip()

# -------------------------
# MODEL QUERY
# -------------------------
def query_model(prompt):
    try:
        client = get_hf_client()

        response = client.chat_completion(
            messages=[
                {"role": "system", "content": "You are a certified professional fitness trainer."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=1600,
            temperature=0.7,
            top_p=0.9
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        return f"⚠️ Model Error: {str(e)}"

# =========================
# PAGE 1 → FORM
# =========================
if st.session_state.page == "form":

    with st.form("fitness_form"):

        st.subheader("Personal Information")

        name = st.text_input("Full Name*", placeholder="Enter your name")

        age = st.number_input("Age*", min_value=18, max_value=65, step=1)

        col1, col2 = st.columns(2)
        with col1:
            height = st.number_input("Height (cm)*", min_value=1.0, step=0.1)
        with col2:
            weight = st.number_input("Weight (kg)*", min_value=1.0, step=0.1)

        st.subheader("Fitness Details")

        goal = st.selectbox(
            "Fitness Goal",
            ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexibility"]
        )

        level = st.radio(
            "Fitness Level",
            ["Beginner", "Intermediate", "Advanced"]
        )

        equipment = st.multiselect(
            "Available Equipment",
            ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment", 
             "Kettlebell", "Pull-up Bar"]
        )

        submit = st.form_submit_button("Submit Profile")

    # -------------------------
    # HANDLE SUBMISSION
    # -------------------------
    if submit:

        if not name:
            st.error("Please enter your name.")

        elif height <= 0 or weight <= 0:
            st.error("Please enter valid height and weight.")

        elif not equipment:
            st.error("Please select at least one equipment option.")

        else:
            # Store in session
            st.session_state.name = name
            st.session_state.age = age
            st.session_state.height = height
            st.session_state.weight = weight
            st.session_state.goal = goal
            st.session_state.level = level
            st.session_state.equipment = equipment

            st.session_state.page = "result"
            st.rerun()

# =========================
# PAGE 2 → RESULT
# =========================
if st.session_state.page == "result":

    name = st.session_state.name
    age = st.session_state.age
    height = st.session_state.height
    weight = st.session_state.weight
    goal = st.session_state.goal
    level = st.session_state.level
    equipment = st.session_state.equipment

    st.success("Profile Submitted Successfully!")

    bmi = calculate_bmi(weight, height)
    bmi_status = get_category(bmi)

    st.write("## 📋 Your Personal Information")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Height:** {height} cm")
    st.write(f"**Weight:** {weight} kg")
    st.write(f"**BMI:** {bmi} ({bmi_status})")
    st.write(f"**Goal:** {goal}")
    st.write(f"**Fitness Level:** {level}")
    st.write(f"**Equipment:** {', '.join(equipment)}")

    with st.spinner("Generating your 5-day workout plan..."):
        prompt = build_prompt(
            name=name,
            age=age,
            height=height,
            weight=weight,
            goal=goal,
            level=level,
            equipment=equipment,
            bmi=bmi,
            bmi_status=bmi_status
        )

        full_plan = query_model(prompt)

    st.subheader("🏋️ Your Personalized 5-Day Workout Plan")
    st.write(full_plan)

    if st.button("⬅️ Back"):
        st.session_state.page = "form"
        st.rerun()
