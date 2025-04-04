
# Object Detection Scripts for Gravestein Vision

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

## Integration with the Web Application:

The front-end application is already set up to make API calls for object detection. To connect it with these Python scripts, you need to create a simple backend that:

1. Accepts image uploads from the front-end
2. Calls the `detect_objects_web()` function from `web_detector.py`
3. Returns the results to the front-end

### Example Backend Setup (Python Flask):

```python
from flask import Flask, request, jsonify
from flask_cors import CORS
import sys
import os

# Add the scripts directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), 'scripts'))

# Import the web detector function
from web_detector import detect_objects_web

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/detect', methods=['POST'])
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

The current front-end is using a mock API that simulates object detection. To use the actual Python-based detection, you'll need to:

1. Set up the backend server with Flask or another Python web framework
2. Update the front-end API calls to point to your backend server
3. Ensure all Python dependencies are installed on the server
