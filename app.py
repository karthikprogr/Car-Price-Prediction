from flask import Flask, request, render_template
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model
with open('car_prediction.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get user inputs from form
        user_input = {
            "Company": request.form['company'],
            "City": request.form['city'],
            "Year": float(request.form['year']),
            "KM_Driven": float(request.form['km_driven']),
            "No_of_Owners": float(request.form['num_owners']),
            "Fuel_Type": float(request.form['fuel_type']),
            "Calculated_Score": float(request.form['calculated_score'])
        }

        # Convert categorical variables (Company & City) to numerical using hashing
        company_hash = hash(user_input["Company"]) % 1000
        city_hash = hash(user_input["City"]) % 1000

        # Prepare features (ensuring 11 input features)
        features = np.array([[ 
            company_hash, 
            city_hash, 
            user_input["Year"], 
            np.log1p(user_input["KM_Driven"]), 
            user_input["No_of_Owners"], 
            user_input["Fuel_Type"], 
            user_input["Calculated_Score"], 
            user_input["Year"] * city_hash, 
            np.log1p(user_input["KM_Driven"]) * user_input["No_of_Owners"], 
            user_input["Year"] ** 2, 
            np.log1p(user_input["KM_Driven"]) ** 2
        ]])

        # Predict the price
        prediction = model.predict(features)
        result = f"Predicted Price: ₹{round(prediction[0], 2)}"
    
    except Exception as e:
        result = f"Error in prediction: {e}"

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
