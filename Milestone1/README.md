Milestone 1: Fitness Profile & BMI Generator

Objective
The objective of this milestone is to develop a user-friendly front-end fitness profile form using Streamlit. The application is designed to capture essential user health details, implement accurate BMI calculation logic, and classify results into standard health categories.

BMI Formula Explanation
The Body Mass Index (BMI) is calculated using the standard metric formula. 

1. Height Conversion: Since input is collected in centimeters, it is converted to meters:  
   *Height (m) = Height (cm) / 100*
   
2. Calculation: The weight in kilograms is divided by the square of the height in meters:  
   *BMI = weight (kg) / (height (m)²)*

3. Rounding: The final BMI value is rounded to two decimal places for clarity.

Steps Performed
- Form Creation: Created a structured layout using `st.form` to group personal info and fitness goals.
- Validation: Added logic to ensure the "Name" field is not empty and that "Height" and "Weight" are positive numbers.
- BMI Logic: Wrote Python functions to process the math and return the corresponding health category (Underweight, Normal, Overweight, or Obese).
- Deployment: Configured the `requirements.txt` file and pushed the code to GitHub, then synced it with Hugging Face Spaces.

Technologies Used
- Python: Core programming logic.
- Streamlit: Web framework for the user interface.
- Hugging Face Spaces: Cloud hosting platform.
- GitHub: Version control and repository management.

Live Demo: https://huggingface.co/spaces/srustik123/FitPlan_AI_Personalized_Fitness_Plan_Generator

Screenshots of the Running Application
<img width="1913" height="962" alt="image" src="https://github.com/user-attachments/assets/da04916f-baa2-4de4-b0df-cdffdaca75a9" />
