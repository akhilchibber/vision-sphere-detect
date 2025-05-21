import sys
import os
from flask import Flask, request, jsonify
from flask_cors import CORS

# Add the 'src' directory to sys.path, assuming 'app.py' is in 'backend/'
# and 'scripts' is in 'src/' at the same level as 'backend/'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# Now you should be able to import from src.scripts
from src.scripts.web_detector import detect_objects_web

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/detect', methods=['POST'])
def detect():
    if 'image' not in request.files:
        return jsonify({'error': 'No image provided'}), 400
    
    image_file = request.files['image']
    
    # Ensure the image_file is a valid image file (e.g., by checking extension or content type)
    # For simplicity, this example assumes the file is a valid image.
    
    try:
        # Call detect_objects_web with the image file
        results = detect_objects_web(image_file)
        return jsonify(results)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
