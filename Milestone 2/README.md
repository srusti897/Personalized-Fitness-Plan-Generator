# 💪 FitPlan-AI

FitPlan-AI is an AI-powered personalized fitness assistant that generates structured 5-day workout plans based on user inputs such as BMI, fitness goal, fitness level, and available equipment.

##🚀 Objective of the Milestone

The objective of this milestone was to:
- Build an AI-driven personalized fitness planner  
- Dynamically calculate BMI from user inputs  
- Generate structured 5-day workout plans using a Large Language Model (LLM)  
- Integrate Hugging Face Transformers with Streamlit  
- Deploy the application using Hugging Face Spaces  

The system combines prompt engineering, model inference, and an interactive web interface to deliver personalized fitness plans.

##  Model Used
Model Name: `Qwen/Qwen2.5-7B-Instruct`

### Why This Model?
- Instruction-tuned Transformer model  
- Encoder–Decoder architecture  
- Generates structured formatted outputs  
- Capable of handling long multi-day workout plans  
- More reliable than smaller models for detailed responses  

The model is loaded using Hugging Face Transformers and optimized with proper generation parameters.

## System Architecture
1. User enters personal and fitness details in the Streamlit interface  
2. BMI is calculated dynamically  
3. A structured prompt is generated using user data  
4. The Large Language Model generates a 5-day personalized workout plan  
5. The output is displayed in the Streamlit app  

##  Prompt Design Strategy
The prompt was carefully engineered to:

- Assign a clear role to the model  
  ```
  You are a certified professional fitness trainer.
  ```

- Enforce strict formatting for structured output  
  ```
  STRICT FORMAT:
  Day 1:
  - Warm-up:
  - Exercises:
  - Rest:
  - Cool Down:
  ```

- Include personalized user information:
  - BMI and BMI category  
  - Fitness goal  
  - Fitness level  
  - Available equipment  

- Prevent repetition of instructions  
  ```
  Do NOT repeat instructions.
  Start directly with Day 1.
  ```

This structured prompt ensures detailed, personalized, and properly formatted workout plans.

###  Model Loading
The model and tokenizer are loaded using Hugging Face Transformers:

```python
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-large")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-large")
```
Streamlit caching is used to avoid reloading the model on every interaction:
```python
@st.cache_resource

###  BMI Calculation
BMI formula used:
BMI = weight / (height in meters)^2
BMI Categories:
- < 18.5 → Underweight  
- 18.5 – 24.9 → Normal  
- 25 – 29.9 → Overweight  
- ≥ 30 → Obese  

###  Prompt Creation
A dynamic prompt is generated using:
- Name  
- Height and Weight and age
- Calculated BMI and category  
- Fitness goal  
- Fitness level  
- Available equipment  
The prompt ensures the model generates a structured 5-day workout plan.

###  Inference Testing
Model generation parameters:

```python
outputs = model.generate(
    **inputs,
    max_new_tokens=1600,
    temperature=0.7,
    do_sample=True,
    repetition_penalty=1.1
)

Parameter Explanation:
- `max_new_tokens=1600` → Allows long structured output  
- `temperature=0.7` → Balanced creativity  
- `do_sample=True` → Enables variation  
- `repetition_penalty=1.1` → Reduces repetition  

##  Sample Generated Output

Input:

- Height: 165 cm  
- Weight: 54 kg  
-Age : 18
- Goal: Build Muscle  
- Fitness Level: Beginner  
- Equipment: Dumbbells, Yoga Mat  

**Generated Output:**

```
Day 1:
- Warm-up: 5 min light jogging
- Dumbbell Squats – 3 × 12
- Push-ups – 3 × 10
- Plank – 3 × 30 sec
- Rest: 60 seconds
- Cool Down: Stretching

Day 2:
- Lunges – 3 × 12
- Shoulder Press – 3 × 10
- Bicycle Crunch – 3 × 15
...

Day 3:
...

Day 4:
...

Day 5:
...
```

The plan adjusts intensity and exercise selection based on BMI, fitness level, and available equipment.

---

## Deployment

The application is deployed using Hugging Face Spaces with Streamlit.

Live Demo:  https://huggingface.co/spaces/srustik123/Module_2
---

## 👩‍💻 Author

Developed as part of an AI milestone project.
