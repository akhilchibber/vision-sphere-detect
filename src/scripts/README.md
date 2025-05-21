
# Object Detection Scripts for Gravestein Vision

**Important Note:** The primary, fully functional backend for this application is now located in the `backend/` directory (`backend/app.py`). The Flask example provided below is a minimalistic illustration of how `web_detector.py` can be used, but for running the complete application, please refer to the main project README and the `backend/` directory.

This directory contains Python scripts for object detection using YOLOv5.

## Files:

1. `object_detection.py` - The original standalone script that works with local files
2. `web_detector.py` - A modified version that can be used with a web API

## Requirements:

To use these scripts, you need to install the following Python packages:
```
torch
opencv-python
numpy
pandas
Pillow
```

## `web_detector.py` Details:

The `detect_objects_web(image_data, model_name)` function in `web_detector.py` is designed to be called from a web API.

*   **Arguments:**
    *   `image_data`: Raw image data (bytes) from an upload, or a file path.
    *   `model_name` (optional): Name of the YOLOv5 model to use (e.g., `yolov5s`).
*   **Returns:**
    A dictionary with the following structure:
    ```json
    {
      "imageUrl": "data:image/jpeg;base64,...", // Base64 encoded image with detections drawn
      "detections": [
        {
          "label": "object_name", // e.g., "person", "car"
          "confidence": 0.85,     // Detection confidence score
          "box": {
            "x": 100,
            "y": 150,
            "width": 50,
            "height": 75
          }
        }
        // ... more detections
      ],
      "object_count": 5 // Total number of objects detected
    }
    ```
    If an error occurs, it returns `{"error": "Error message"}`.

## Integration with a Web Application:

To use these scripts in a web application, you need a backend that:

1. Accepts image uploads.
2. Calls the `detect_objects_web()` function from `web_detector.py`.
3. Returns the JSON results to the frontend.

### Minimalistic Flask Example:

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

# Import the web detector function
# Ensure web_detector.py is in the same directory or accessible via sys.path
from web_detector import detect_objects_web 

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/minimal_api/detect', methods=['POST']) # Renamed endpoint for clarity
def detect():
    if 'image' not in request.files:
        return jsonify({"error": "No image file provided"}), 400
    
    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No image file selected"}), 400
    
    # Read the image data
    image_data = file.read()
    
    # Call the detection function
    result = detect_objects_web(image_data)
    
    # Return the result
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
```

## Note:

As mentioned, the main application backend is in `backend/app.py`. That backend is already configured to work with the frontend. The example above is for understanding how `web_detector.py` can be used independently or for testing purposes.
