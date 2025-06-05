# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# import os

# # Load the trained model
# try:
#     model_path = os.path.join(os.path.dirname(__file__), 'car_prediction.pkl')
#     model = pickle.load(open(model_path, 'rb'))
# except Exception as e:
#     print(f"Error loading model: {e}")
#     model = None

# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict_price():
#     if model is None:
#         return render_template('index.html', result="Model not loaded. Check the file path.")

#     try:
#         year = int(request.form.get('year', 0))
#         km_driven = int(request.form.get('km_driven', 0))
#         num_owners = int(request.form.get('num_owners', 0))
#         fuel_type = int(request.form.get('fuel_type', 0))
#         calculated_score = float(request.form.get('calculated_score', 0.0))

#         input_features = np.array([[year, km_driven, num_owners, fuel_type, calculated_score]])
#         result = model.predict(input_features)[0]
#         return render_template('index.html', result=f'Predicted Price: {result:.2f} Lakhs')

#     except ValueError:
#         return render_template('index.html', result="Invalid input, please enter valid numbers.")
#     except Exception as e:
#         return render_template('index.html', result=f"Error in prediction: {str(e)}")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)


# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# import os

# # Load the trained model
# try:
#     model_path = os.path.join(os.path.dirname(__file__), 'car_prediction.pkl')
#     model = pickle.load(open(model_path, 'rb'))
#     print("Model loaded successfully!")
# except Exception as e:
#     print(f"Error loading model: {e}")
#     model = None

# # Initialize Flask app
# app = Flask(__name__)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict_price():
#     if model is None:
#         return render_template('index.html', result="Model not loaded. Check the file path.")

#     try:
#         # Get input values from form
#         year = request.form.get('year')
#         km_driven = request.form.get('km_driven')
#         num_owners = request.form.get('num_owners')
#         fuel_type = request.form.get('fuel_type')
#         calculated_score = request.form.get('calculated_score')

#         # Print input values for debugging
#         print(f"Received inputs - Year: {year}, KM Driven: {km_driven}, Owners: {num_owners}, Fuel: {fuel_type}, Score: {calculated_score}")

#         # Validate inputs
#         if not (year and km_driven and num_owners and fuel_type and calculated_score):
#             return render_template('index.html', result="Please fill in all fields.")

#         # Convert inputs to appropriate data types
#         try:
#             year = int(year)
#             km_driven = int(km_driven)
#             num_owners = int(num_owners)
#             fuel_type = int(fuel_type)
#             calculated_score = float(calculated_score)
#         except ValueError:
#             return render_template('index.html', result="Invalid input, please enter valid numbers.")

#         # Transform features (if required by the model)
#         log_km_driven = np.log1p(km_driven)
#         year_city = year * 1  # Adjust if your model uses a different encoding
#         km_owners = log_km_driven * num_owners

#         # Create feature array
#         input_features = np.array([[year, num_owners, fuel_type, calculated_score, log_km_driven, year_city, km_owners]])

#         # Ensure input shape matches model expectation
#         print(f"Input shape: {input_features.shape}")

#         # Make prediction
#         result = model.predict(input_features)[0]

#         return render_template('index.html', result=f'Predicted Price: {result:.2f} Lakhs')

#     except Exception as e:
#         return render_template('index.html', result=f"Error in prediction: {str(e)}")

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=8000, debug=True)







# from flask import Flask, request, render_template
# import numpy as np
# import pickle

# app = Flask(__name__)

# # Load the trained model
# with open('car_prediction.pkl', 'rb') as f:
#     model = pickle.load(f)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/predict', methods=['POST'])
# def predict():
#     try:
#         # Get user inputs from form
#         user_input = {
#             "Company": float(request.form['company']),
#             "City": float(request.form['city']),
#             "Year": float(request.form['year']),
#             "KM_Driven": float(request.form['km_driven']),
#             "No_of_Owners": float(request.form['num_owners']),
#             "Fuel_Type": float(request.form['fuel_type']),
#             "Calculated_Score": float(request.form['calculated_score'])
#         }

#         # Prepare features (ensuring 11 input features)
#         features = np.array([[ 
#             user_input["Company"], 
#             user_input["City"], 
#             user_input["Year"], 
#             np.log1p(user_input["KM_Driven"]), 
#             user_input["No_of_Owners"], 
#             user_input["Fuel_Type"], 
#             user_input["Calculated_Score"], 
#             user_input["Year"] * user_input["City"], 
#             np.log1p(user_input["KM_Driven"]) * user_input["No_of_Owners"], 
#             user_input["Year"] ** 2, 
#             np.log1p(user_input["KM_Driven"]) ** 2
#         ]])

#         # Predict the price
#         prediction = model.predict(features)
#         result = f"Predicted Price: ₹{round(prediction[0], 2)}"
    
#     except Exception as e:
#         result = f"Error in prediction: {e}"

#     return render_template('index.html', result=result)

# if __name__ == '__main__':
#     app.run(debug=True)



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
