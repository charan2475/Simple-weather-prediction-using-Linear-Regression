import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample weather data (replace this with your own dataset)
# The data should contain features (e.g., temperature, humidity) and the target variable (e.g., temperature for the next day).
data = {
    'temperature': [25, 28, 30, 32, 29, 27],
    'humidity': [50, 55, 60, 65, 70, 75],
    'pressure': [1015, 1016, 1017, 1018, 1019, 1020],
    'target_temperature': [28, 30, 32, 29, 27, 26]  # Target variable: temperature for the next day
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Separate features and target variable
X = df[['temperature', 'humidity', 'pressure']]
y = df['target_temperature']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model and fit it to the data
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Example usage: predict temperature for a new set of features
new_features = np.array([[26, 60, 1018]])
predicted_temperature = model.predict(new_features)
print(f"Predicted temperature for the next day: {predicted_temperature[0]:.2f}°C")
