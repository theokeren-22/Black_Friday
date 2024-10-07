import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

data = pd.read_csv('model.csv')

x = data[['Age', 'City_Category', 'Stay_In_Current_City_Years', 'Product_Category_1', 'Product_Category_2', 'Product_Category_3']]
y = data['Purchase']

print(x.columns)
print(y)

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators = 500, random_state=42)
rf_model.fit(x_train, y_train)

# Step 5: Save the model to a .pkl file
with open('model.pkl', 'wb') as file:
    pickle.dump(rf_model, file)

print("Model trained and saved as model.pkl")