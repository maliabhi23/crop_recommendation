
from flask import Flask, request, render_template
import joblib
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
# .\venv\Scripts\activate

model = joblib.load('cropappe')

# Route to display the form (front-end)
@app.route('/')
def home():
    return render_template('index.html')

# Route to handle form submission and return the prediction
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from the form
        nitrogen = float(request.form['nitrogen'])
        phosphorus = float(request.form['phosphorus'])
        potassium = float(request.form['potassium'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        ph_value = float(request.form['ph_value'])
        rainfall = float(request.form['rainfall'])

        # Prepare the input features for prediction
        features = [[nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]]
        print(features)
        # Use the model to make a prediction
        prediction = model.predict(features)
        print(prediction[0])
        # Map the prediction to the corresponding crop (adjust according to your model's output)
        # crop_mapping = {
        #     0: "Crop 1",  # Replace with actual crop names
        #     1: "Crop 2",
        #     2: "Crop 3",
        #     # Add more crop mappings as per your model output
        # }
        #
        # predicted_crop = crop_mapping.get(prediction[0], "Unknown Crop")

        # Return the prediction result
        return render_template('result.html', crop=prediction)

    except Exception as e:
        return f"Error during prediction: {e}"

# Run the app

if __name__ == '__main__':
     app.run(host='0.0.0.0', port=5000,debug=True)
# means the run this file __name__ set ti the __main__ them this cpde use on the other module when call dome them