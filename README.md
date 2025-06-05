# 🚗 Car Price Predictor – Know Your Car’s Worth with AI


This project uses machine learning to predict the selling price of a car based on various features like year, brand, fuel type, transmission, kilometers driven, and more. It helps users estimate a fair price for used cars, aiding both sellers and buyers.

---

## 📌 About the Project

Buying or selling a car can be tricky without knowing its actual market value. This Car Price Predictor uses real-world data and a trained machine learning model to make accurate price predictions based on car features. The model is trained on a dataset containing details of used cars listed for sale.

---

## 💡 Features

- Predict the price of a used car
- Inputs: Car brand, year, kilometers driven, fuel type, seller type, transmission, etc.
- Uses regression algorithms to give price estimation
- Web app interface using Flask
- Clean visualization of predictions
- Instant predictions with pre-trained model

---

## 🔧 Technologies Used

- Python 🐍
- Flask 🌐
- Pandas & NumPy 📊
- Scikit-learn 🤖
- Matplotlib 📈
- Pickle (for model serialization) 📦
- HTML/CSS for the front end 🖥️

---

## 🚀 Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/car-price-prediction.git
```
2. Navigate to the project folder:

```bash
cd car-price-prediction
```pip install -r requirements.txt
```
python app.py

## 📲 Usage

- Open your browser and go to `http://127.0.0.1:5000`
- Enter the car details like Year, Brand, Fuel Type, etc.
- Click on **Predict**
- The model will display the estimated resale price of the car.

---

## 📊 Model Details

- Dataset used: 6000+ records of used cars.
- Preprocessing steps:
  - Handled missing values
  - Label encoded categorical variables
  - Feature scaling and transformation
- Models tested:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor ✅ *(used for deployment)*
- Final R² score: ~94%

---

## 🙌 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature/bugfix branch
3. Make your changes and commit with a meaningful message
4. Push the branch and open a pull request

---

## 📬 Contact

Feel free to reach out:

- 📧 Email: [seelamkarthik2006@gmail.com](seelamkarthik2006@gmail.com)

---

> 🔍 Predict your car's price accurately before you buy or sell!
