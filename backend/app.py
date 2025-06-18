from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import sys

# Add the scripts directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "..", "src", "scripts"))

from web_detector import detect_objects_web

app = Flask(__name__)
CORS(app)


@app.route("/api/detect", methods=["POST"])
def detect():
    if "image" not in request.files:
        return jsonify({"error": "No image file provided"}), 400

    file = request.files["image"]
    if file.filename == "":
        return jsonify({"error": "No image file selected"}), 400

    image_data = file.read()
    result = detect_objects_web(image_data)

    return jsonify(result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
