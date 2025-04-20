from flask import Flask, request, jsonify
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! Use /predict?W=1&X=20 to get prediction."

@app.route("/predict", methods=["GET"])
def predict():
    try:
        W = float(request.args.get("W"))
        X = float(request.args.get("X"))
        input_data = np.array([[1, W, X]])
        prediction = model.predict(input_data)[0]
        return jsonify({"predicted_engagement_score": round(prediction, 2)})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
