import numpy as np
import pandas as pd
from flask import Flask, request, render_template
from sklearn.preprocessing import StandardScaler
from sklearn import svm
import pickle
import os

app = Flask(__name__)

# Load the model and scaler
def load_model():
    # Train the model if it doesn't exist
    if not os.path.exists('diabetes_model.pkl'):
        # Load the dataset
        diabetes_dataset = pd.read_csv('diabetes.csv')
        
        # Separate features and target
        X = diabetes_dataset.drop(columns='Outcome', axis=1)
        Y = diabetes_dataset['Outcome']
        
        # Standardize the data
        scaler = StandardScaler()
        scaler.fit(X)
        X_standardized = scaler.transform(X)
        
        # Train the model
        classifier = svm.SVC(kernel='linear')
        classifier.fit(X_standardized, Y)
        
        # Save the model and scaler
        with open('diabetes_model.pkl', 'wb') as model_file:
            pickle.dump(classifier, model_file)
        with open('scaler.pkl', 'wb') as scaler_file:
            pickle.dump(scaler, scaler_file)
    
    # Load the model and scaler
    with open('diabetes_model.pkl', 'rb') as model_file:
        model = pickle.load(model_file)
    with open('scaler.pkl', 'rb') as scaler_file:
        scaler = pickle.load(scaler_file)
    
    return model, scaler

# Load model at startup
model, scaler = load_model()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Get form data
    features = [float(request.form.get(feature)) for feature in [
        'pregnancies', 'glucose', 'bloodpressure', 'skinthickness',
        'insulin', 'bmi', 'diabetespedigreefunction', 'age'
    ]]
    
    # Convert to numpy array and reshape
    input_data = np.asarray(features).reshape(1, -1)
    
    # Standardize the input data
    std_data = scaler.transform(input_data)
    
    # Make prediction
    prediction = model.predict(std_data)
    
    # Determine result
    result = "Diabetic" if prediction[0] == 1 else "Not Diabetic"
    
    return render_template('result.html', 
                          prediction=result, 
                          features=dict(zip([
                              'Pregnancies', 'Glucose', 'Blood Pressure', 'Skin Thickness',
                              'Insulin', 'BMI', 'Diabetes Pedigree Function', 'Age'
                          ], features)))

if __name__ == '__main__':
    app.run(debug=True)