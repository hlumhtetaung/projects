import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Define the dataset as a DataFrame
data = {
    'Square_Feet': [1200, 1500, 850, 2200, 1800, 1350, 2600, 950, 1650, 2000, 1100, 2400, 1700, 2900, 1400],
    'Bedrooms': [2, 3, 1, 4, 3, 2, 4, 2, 3, 3, 2, 4, 3, 5, 3],
    'Age_Years': [15, 10, 25, 5, 12, 18, 2, 30, 8, 14, 22, 6, 11, 1, 16],
    'Distance_City_Miles': [12.5, 8.0, 15.2, 5.0, 6.5, 10.0, 3.1, 18.0, 7.2, 4.5, 14.0, 2.8, 9.0, 1.5, 11.0],
    'Price_USD': [210000, 275000, 140000, 410000, 330000, 230000, 490000, 155000, 305000, 360000, 185000, 450000, 295000, 560000, 245000]
}

df = pd.DataFrame(data)

# Display the DataFrame
print(df)

# Simple Linear Regression using only two columns (features dependent and independent)
predictor = df['Square_Feet']
outcome = df['Price_USD']

model = LinearRegression()
model.fit(predictor.values.reshape(-1, 1), outcome)

print(f"Intercept: {model.intercept_:.3f}")
print(f"Slope: {model.coef_[0]:.3f}")

# Visualizing the regression line
plt.scatter(predictor, outcome, color='blue')
plt.plot(predictor, model.predict(predictor.values.reshape(-1, 1)), color='red')
plt.title('Simple Linear Regression: Price vs Square Feet')
plt.xlabel('Square Feet')
plt.ylabel('Price (USD)')
plt.show()