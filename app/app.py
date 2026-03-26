from  flask import Flask, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

#load model
model = pickle.load(open("../models/model.pkl", "rb"))

@app.route("/")
def home():
    return "House price prediction api is running!"

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    
    #expects : [area , bedrooms , bathrooms , location]
    features = np.array([data["features"]])
    
    prediction = model.predict(features)
    
    return jsonify({
        "predicted_price": prediction.tolist()
    })
    
if __name__== "__main__":
    app.run(debug=True)
    
