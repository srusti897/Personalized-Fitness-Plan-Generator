import streamlit as st

def calculate_bmi(weight, height_cm):
    # Convert height from cm to meters
    height_m = height_cm / 100
    # BMI formula: weight (kg) / (height in meters)^2
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

# App UI
st.set_page_config(page_title="FitPlan-AI", page_icon="💪")
st.title("💪 FitPlan-AI: Personalized Fitness Profile")

with st.form("fitness_form"):
    st.header("Personal Information")
    name = st.text_input("Full Name*", placeholder="Enter your name")
    
    col1, col2 = st.columns(2)
    with col1:
        height = st.number_input("Height (cm)*", min_value=1.0, step=0.1)
    with col2:
        weight = st.number_input("Weight (kg)*", min_value=1.0, step=0.1)

    st.header("Fitness Details")
    goal = st.selectbox("Fitness Goal", ["Build Muscle", "Weight Loss", "Strength Gain", "Abs Building", "Flexible"])
    level = st.radio("Fitness Level", ["Beginner", "Intermediate", "Advanced"])
    equipment = st.multiselect("Available Equipment", ["Dumbbells", "Resistance Band", "Yoga Mat", "No Equipment", "Kettlebell", "Pull-up Bar"])

    submit = st.form_submit_button("Generate Profile")

if submit:
    # Validation: Ensure name is not empty
    if not name.strip():
        st.error("Please enter your name.")
    elif height <= 0 or weight <= 0:
        st.error("Height and Weight must be positive values.")
    else:
        # BMI Logic
        user_bmi = calculate_bmi(weight, height)
        category = get_category(user_bmi)
        
        # Display Results
        st.success(f"Profile Created Successfully for {name}!")
        st.metric(label="Your Calculated BMI", value=user_bmi)
        st.info(f"Health Category: **{category}**")
        
        # Summary
        st.write(f"**Goal:** {goal} | **Level:** {level}")
        st.write(f"**Equipment:** {', '.join(equipment) if equipment else 'None selected'}")
