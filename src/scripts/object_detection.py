
# -----------------------------------------------------------------------------
# Object Detection Script using YOLOv5 and OpenCV
# -----------------------------------------------------------------------------
# Purpose:
# This script loads a pre-trained YOLOv5 object detection model,
# uses it to detect objects in a specified input image,
# and displays the image with bounding boxes drawn around the detected objects.
# -----------------------------------------------------------------------------

# --- Step 0: Import Necessary Libraries ---
import torch  # PyTorch library for deep learning, used here to load the YOLOv5 model.
import cv2    # OpenCV library for computer vision tasks like reading/displaying images and drawing shapes.
import os     # Operating system library for interacting with the file system (e.g., joining paths).
from PIL import Image # Python Imaging Library, often used for image manipulation (though not directly used in the main flow here, might be a dependency).

# --- Configuration ---
# Description: Modify these variables to change the input image or the model used.
# -----------------------------------------------------------------------------
INPUT_IMAGE_FOLDER = "input_images" # Folder where the input image is located.
IMAGE_FILENAME = "train.jpg" # The specific name of the image file to process within INPUT_IMAGE_FOLDER.
                           # Make sure you place an image with this name in the input folder.
MODEL_NAME = 'yolov5s'     # The specific YOLOv5 model variant to use.
                           # Options include: 'yolov5s' (small, fast), 'yolov5m' (medium),
                           # 'yolov5l' (large), 'yolov5x' (extra-large, most accurate but slowest).
                           # The chosen model will be downloaded if not already present locally.
# -----------------------------------------------------------------------------


# --- Main Detection Function ---
def detect_objects():
    """
    Loads a YOLOv5 model, performs object detection on a single image,
    draws bounding boxes around detected objects, and displays the result.
    """

    # --- Step 1: Prepare Image Path and Check Existence ---
    # Construct the full path to the input image.
    image_path = os.path.join(INPUT_IMAGE_FOLDER, IMAGE_FILENAME)
    print(f"Attempting to load image: {image_path}")

    # Verify that the image file actually exists at the specified path.
    if not os.path.exists(image_path):
        print(f"Error: Image not found at {image_path}")
        print(f"Please place an image named '{IMAGE_FILENAME}' inside the '{INPUT_IMAGE_FOLDER}' directory.")
        return # Exit the function if the image is not found.

    # --- Step 2: Load the YOLOv5 Model ---
    # Description: This step loads the specified YOLOv5 model architecture and weights.
    # Source: The model is loaded from PyTorch Hub, a repository for pre-trained models.
    # Download: If the model (e.g., 'yolov5s.pt') is not found in the local PyTorch cache,
    #           torch.hub.load will attempt to DOWNLOAD it from the internet.
    # Parameters:
    #   'ultralytics/yolov5': The repository path on GitHub/PyTorch Hub.
    #   MODEL_NAME: The specific model variant (e.g., 'yolov5s') defined in the configuration.
    #   pretrained=True: Specifies that we want the model weights pre-trained on the COCO dataset.
    #   force_reload=False: Tries to use the cached model first. Set to True to force a re-download.
    print(f"Loading YOLOv5 model: '{MODEL_NAME}'...")
    try:
        # Attempt to load the model (may download if not cached)
        model = torch.hub.load('ultralytics/yolov5', MODEL_NAME, pretrained=True, force_reload=False)
        print("Model loaded successfully.")
    except Exception as e:
        # Handle potential errors during model loading (e.g., network issues, cache problems).
        print(f"Error loading model '{MODEL_NAME}': {e}")
        print("Trying again with force_reload=True (this will force a re-download)...")
        try:
            # Retry loading, forcing a download/overwrite of the cache.
            model = torch.hub.load('ultralytics/yolov5', MODEL_NAME, pretrained=True, force_reload=True)
            print("Model loaded successfully with force_reload=True.")
        except Exception as e_reload:
             # If loading fails even with force_reload, inform the user and exit.
             print(f"Error loading model even with force_reload: {e_reload}")
             print("Please check your internet connection, PyTorch Hub access, and model name validity.")
             return # Exit the function if the model cannot be loaded.

    # --- Step 3: Load the Image using OpenCV ---
    # Read the image file from the specified path using OpenCV.
    # OpenCV loads images in BGR (Blue, Green, Red) color format by default.
    img_cv = cv2.imread(image_path)
    # Check if the image was loaded successfully.
    if img_cv is None:
        print(f"Error: Could not read image file {image_path} with OpenCV.")
        print("The file might be corrupted or in an unsupported format.")
        return # Exit if the image cannot be read.
    print(f"Image '{IMAGE_FILENAME}' loaded successfully.")

    # --- Step 4: Preprocess the Image ---
    # Convert the image color format from BGR (OpenCV default) to RGB (Red, Green, Blue).
    # Most PyTorch models, including YOLOv5, expect images in RGB format.
    img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
    print("Image color space converted from BGR to RGB.")

    # --- Step 5: Perform Object Detection (Inference) ---
    # Pass the RGB image (or a list of images) to the loaded model.
    # The model performs a forward pass and returns detection results.
    print("Performing object detection...")
    results = model(img_rgb)
    print("Detection complete.")

    # --- Step 6: Process Detection Results ---
    # The 'results' object contains information about detected objects.

    # Print a summary of the detections to the console (e.g., "image 1/1: 640x480 1 person, 1 dog").
    print("\n--- Detection Summary ---")
    results.print()
    print("-------------------------\n")

    # Optionally, display results in a separate window managed by the YOLOv5 library.
    # This is an alternative to drawing boxes manually with OpenCV.
    # results.show()

    # Extract detailed detection results into a pandas DataFrame for easier access.
    # results.pandas().xyxy[0] provides bounding boxes in (xmin, ymin, xmax, ymax) format
    # along with confidence scores and class names for the first (and only) image.
    df = results.pandas().xyxy[0] # predictions (pandas)
    print(f"Found {len(df)} objects.")
    # print("\n--- Detailed Detections (Pandas DataFrame) ---")
    # print(df)
    # print("----------------------------------------------\n")


    # --- Step 7: Draw Bounding Boxes and Labels on the Image ---
    # Iterate through each detected object found in the DataFrame.
    print("Drawing bounding boxes and labels on the image...")
    for index, row in df.iterrows():
        # Extract detection data for the current object.
        # Coordinates are cast to integers as pixel values must be integers.
        xmin, ymin, xmax, ymax = int(row['xmin']), int(row['ymin']), int(row['xmax']), int(row['ymax'])
        confidence = row['confidence'] # The model's confidence score for this detection (0.0 to 1.0).
        name = row['name']             # The detected object's class name (e.g., 'person', 'car').

        # Create the label string to display (e.g., "person: 0.85").
        label = f"{name}: {confidence:.2f}" # Format confidence to 2 decimal places.

        # Define drawing parameters.
        box_color = (0, 255, 0) # Green color for the bounding box (BGR format).
        box_thickness = 2       # Thickness of the bounding box lines.
        font = cv2.FONT_HERSHEY_SIMPLEX # Font type for the label text.
        font_scale = 0.7        # Font size multiplier. Increased for better visibility.
        text_color = (0, 0, 0)  # Black color for the label text (BGR format).
        text_thickness = 1      # Thickness of the label text.

        # Draw the bounding box rectangle on the original BGR image (img_cv).
        cv2.rectangle(img_cv, (xmin, ymin), (xmax, ymax), box_color, box_thickness)

        # --- Calculate text size and position for the label ---
        # Get the width and height of the label text box.
        label_size, base_line = cv2.getTextSize(label, font, font_scale, text_thickness)

        # Calculate the top position for the label, ensuring it doesn't go off the top edge of the image.
        # Place it slightly below the top edge of the bounding box (ymin).
        label_ymin = max(ymin, label_size[1] + 10) # Add a small margin (10 pixels).

        # Draw a filled rectangle as a background for the label text for better readability.
        # The background rectangle starts slightly above the text baseline.
        cv2.rectangle(img_cv,
                      (xmin, label_ymin - label_size[1] - 10), # Top-left corner of background
                      (xmin + label_size[0], label_ymin + base_line - 10), # Bottom-right corner of background
                      box_color, # Use the same color as the box
                      cv2.FILLED) # Fill the rectangle.

        # Put the label text onto the image.
        # Position the text slightly offset within the background rectangle.
        cv2.putText(img_cv, label, (xmin, label_ymin - 7), font, font_scale, text_color, text_thickness)

    print("Finished drawing.")

    # --- Step 8: Display the Final Image ---
    # Create a window to display the image with detections.
    window_name = f"Object Detection Results ({IMAGE_FILENAME})"
    cv2.imshow(window_name, img_cv) # Show the image (which now has boxes drawn on it).

    # Wait indefinitely for the user to press any key in the image window.
    print(f"\nDisplaying results for '{IMAGE_FILENAME}'. Press any key in the '{window_name}' window to close it.")
    cv2.waitKey(0)

    # Close all OpenCV windows that were opened.
    cv2.destroyAllWindows()
    print("Image window closed.")

# --- Script Execution Entry Point ---
# This standard Python construct checks if the script is being run directly
# (not imported as a module into another script).
if __name__ == "__main__":
    # If run directly, call the main detection function.
    print("Script started.")
    detect_objects()
    print("Script finished.")
