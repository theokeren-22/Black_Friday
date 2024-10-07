from flask import Flask, redirect, render_template, request, url_for, Blueprint, session

import pickle

model_pred = Blueprint('model_pred', __name__, template_folder='templates', static_folder='static', static_url_path='/model_prediction/static')

# Load your Random Forest model
def load_model():
    with open('model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model

# Load model once when the application starts
rf_model = load_model()

@model_pred.route('/predict', methods = ['GET', 'POST'])
def predict():
    if 'username' not in session:
        return redirect(url_for('logout'))

    username = session.get('username')
    
    prediction, category_prediction, message = None, None, None
    max_spend_category = None
    personalized_vouchers = None
    
    if request.method == 'POST':
        # Get form data
        age = int(request.form.get('age'))
        product_category_1 = int(request.form.get('product_category_1'))
        product_category_2 = int(request.form.get('product_category_2'))
        product_category_3 = int(request.form.get('product_category_3'))
        city_category = request.form.get('city_category')
        stay_years = request.form.get('stay_years')

        # Prepare input data for prediction
        # Note: This will depend on how your model expects the input data
        input_data = [[age, city_category, stay_years,product_category_1, product_category_2, product_category_3]  ]
        print(input_data)
        # Make prediction
        prediction = int(rf_model.predict(input_data))

        total_weight = product_category_1 + product_category_2 + product_category_3
        if total_weight > 0:
            weights = [ product_category_1 / total_weight,
                        product_category_2 / total_weight,
                        product_category_3 / total_weight ]
        else:
            weights = [ 0, 0, 0]

        category_prediction = [ int(prediction * weights[0]),
                                int(prediction * weights[1]),
                                int(prediction * weights[2]), ]
        
        print(total_weight, weights)

        if (product_category_1 <= 0 and product_category_2 <= 0 and product_category_3 <= 0):
            message = "All the 'Product Categories' are Zero, Atleast fill one."
            return render_template('model_predection.html', 
                                    username = username, 
                                    prediction = None, 
                                    category_prediction = None,
                                    message = message )

        # Calculate maximum spend in different categories
        max_spend_category = max(category_prediction)
        total_purchase_amount = sum(category_prediction)

        print(prediction)
        print(category_prediction)

        # Define discount tiers
        if total_purchase_amount > 5000000:
            discount = 20  # 20% discount
        elif total_purchase_amount > 200000:
            discount = 15  # 15% discount
        elif total_purchase_amount > 100000:
            discount = 10  # 10% discount
        else:
            discount = 5   # 5% discount
        
        if max_spend_category == category_prediction[0]:
            voucher =  "Category 1"
        elif max_spend_category == category_prediction[1]:
            voucher =  "Category 2"
        else:
            voucher =  "Category 3"


        # Create a personalized voucher message
        personalized_vouchers = f"Congratulations, {username}! You have earned a {discount}% discount voucher on your next purchase in {voucher}!"

    return render_template('model_predection.html', 
                            username = username, 
                            prediction = prediction, 
                            category_prediction = category_prediction,
                            max_spend_category = max_spend_category,
                            personalized_vouchers = personalized_vouchers,
                            message = message )

@model_pred.route('/graphs',  methods=['GET'])
def graphs_display():
    if 'username' not in session:
        return redirect(url_for('logout'))

    username = session.get('username')
    return render_template('graphs.html', username = username)