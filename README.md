# Diabetes Prediction System - Static Version

This is a static version of the Diabetes Prediction System, adapted for deployment on Netlify.

## Important Limitations

This static version has the following limitations compared to the original Flask application:

1. **Simulated Predictions**: Since Netlify hosts static sites, the predictions are simulated using JavaScript with a simplified rule-based approach, not the actual SVM model.

2. **No Machine Learning Model**: The original SVM model trained on the diabetes dataset is not used in this version.

3. **Demonstration Only**: This version is for demonstration purposes and should not be used for actual medical predictions or diagnoses.

## How It Works

The static version uses these simplified rules to simulate predictions:
- Glucose > 180 mg/dL → Diabetic
- Glucose > 140 mg/dL AND BMI > 30 kg/m² → Diabetic
- BMI > 35 kg/m² AND Age > 40 years → Diabetic
- Pregnancies > 6 AND Age > 30 years AND BMI > 30 kg/m² → Diabetic

## Deployment Instructions

1. Upload all files to Netlify using the drag-and-drop interface
2. The `netlify.toml` file will configure the site to serve the static_index.html file

## Original Application

The original Flask application includes:
- A trained SVM model with 77% accuracy
- Data standardization using StandardScaler
- Proper model-based predictions

For the full application with accurate predictions, consider deploying to a Python-compatible hosting platform like Heroku, Render, or PythonAnywhere.