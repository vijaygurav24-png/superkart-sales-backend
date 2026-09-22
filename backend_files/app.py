import os
from pathlib import Path

import joblib
import pandas as pd
from flask import Flask, jsonify, request


superkart_api = Flask("superkart_api")
MODEL_PATH = Path(__file__).resolve().parent / "rf_tuned_model.joblib"
model = joblib.load(MODEL_PATH)

REQUIRED_FIELDS = [
    "Product_Weight",
    "Product_Sugar_Content",
    "Product_Allocated_Area",
    "Product_MRP",
    "Store_Size",
    "Store_Location_City_Type",
    "Store_Type",
    "Product_Id_char",
    "Store_Age_Years",
    "Product_Type_Category",
]


@superkart_api.get("/")
def home():
    return "Welcome to SuperKart Sales Prediction API"


@superkart_api.get("/health")
def health():
    return jsonify({"status": "ok", "model": MODEL_PATH.name})


@superkart_api.post("/v1/predict")
def predict_sales():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    missing_fields = [field for field in REQUIRED_FIELDS if field not in data]
    if missing_fields:
        return jsonify({"error": "Missing required fields", "fields": missing_fields}), 400

    input_data = pd.DataFrame([{field: data[field] for field in REQUIRED_FIELDS}])
    prediction = float(model.predict(input_data)[0])
    return jsonify({"Sales": prediction})


if __name__ == "__main__":
    port = int(os.getenv("PORT", "7860"))
    superkart_api.run(host="0.0.0.0", port=port, debug=False)
