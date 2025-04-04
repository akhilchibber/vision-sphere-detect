
# -----------------------------------------------------------------------------
# Object Detection API for Web Application using YOLOv5 and OpenCV
# -----------------------------------------------------------------------------
# This is a modified version of the original object detection script
# that is designed to be called from a web API.
# -----------------------------------------------------------------------------

import torch
import cv2
import os
from PIL import Image
import numpy as np
import base64
from io import BytesIO

# Default model to use
MODEL_NAME = 'yolov5s'

def detect_objects_web(image_data, model_name=MODEL_NAME):
    """
    Process an image from a web upload and return detection results.
    
    Args:
        image_data: Either a file path to the image or raw image data
        model_name: Name of the YOLOv5 model to use
        
    Returns:
        dict: Contains imageData (base64 encoded image with detections) and 
              detections (list of objects found with their coordinates and confidence)
    """
    try:
        # Load the YOLOv5 model
        print(f"Loading YOLOv5 model: '{model_name}'...")
        model = torch.hub.load('ultralytics/yolov5', model_name, pretrained=True, force_reload=False)
        print("Model loaded successfully.")
        
        # Process image data based on input type
        if isinstance(image_data, str) and os.path.exists(image_data):
            # If image_data is a valid file path
            img_cv = cv2.imread(image_data)
            if img_cv is None:
                return {"error": "Could not read image file"}
        else:
            # If image_data is raw data (from web upload)
            nparr = np.frombuffer(image_data, np.uint8)
            img_cv = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
            if img_cv is None:
                return {"error": "Could not decode image data"}
        
        # Convert color space from BGR to RGB
        img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
        
        # Perform object detection
        results = model(img_rgb)
        
        # Get the DataFrame with detection results
        df = results.pandas().xyxy[0]
        
        # Convert DataFrame to a list of detections
        detections = []
        for index, row in df.iterrows():
            detections.append({
                "label": row['name'],
                "confidence": float(row['confidence']),
                "box": {
                    "x": int(row['xmin']),
                    "y": int(row['ymin']),
                    "width": int(row['xmax'] - row['xmin']),
                    "height": int(row['ymax'] - row['ymin'])
                }
            })
        
        # Draw bounding boxes on the image
        for detection in detections:
            xmin = detection["box"]["x"]
            ymin = detection["box"]["y"]
            width = detection["box"]["width"]
            height = detection["box"]["height"]
            xmax = xmin + width
            ymax = ymin + height
            
            name = detection["label"]
            confidence = detection["confidence"]
            
            # Create the label string
            label = f"{name}: {confidence:.2f}"
            
            # Define drawing parameters
            box_color = (0, 255, 0)  # Green color for the bounding box
            box_thickness = 2
            font = cv2.FONT_HERSHEY_SIMPLEX
            font_scale = 0.7
            text_color = (0, 0, 0)  # Black color for text
            text_thickness = 1
            
            # Draw the bounding box
            cv2.rectangle(img_cv, (xmin, ymin), (xmax, ymax), box_color, box_thickness)
            
            # Calculate text size and position
            label_size, base_line = cv2.getTextSize(label, font, font_scale, text_thickness)
            label_ymin = max(ymin, label_size[1] + 10)
            
            # Draw background for text
            cv2.rectangle(img_cv, 
                         (xmin, label_ymin - label_size[1] - 10),
                         (xmin + label_size[0], label_ymin + base_line - 10),
                         box_color,
                         cv2.FILLED)
            
            # Draw the text
            cv2.putText(img_cv, label, (xmin, label_ymin - 7), font, font_scale, text_color, text_thickness)
        
        # Convert the image to base64 for web display
        _, buffer = cv2.imencode('.jpg', img_cv)
        img_base64 = base64.b64encode(buffer).decode('utf-8')
        
        # Return the results
        return {
            "imageUrl": f"data:image/jpeg;base64,{img_base64}",
            "detections": detections
        }
        
    except Exception as e:
        print(f"Error in detect_objects_web: {str(e)}")
        return {"error": str(e)}
