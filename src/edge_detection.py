import cv2  # Import OpenCV library for image processing
import numpy as np  # Import NumPy for numerical operations
import pygame  # Import Pygame for game development and GUI

def apply_edge_detection(image, method):
    # Convert Pygame Surface to OpenCV format
    image_array = pygame.surfarray.array3d(image)  # Convert Pygame surface to a 3D numpy array
    image_array = np.rot90(image_array)  # Rotate the array by 90 degrees to correct orientation
    image_array = np.fliplr(image_array)  # Flip the array left-right to match OpenCV's format
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)  # Convert the image to grayscale

    if method == "canny":
        # Apply Canny edge detection
        # The two numbers (100, 270) are the lower and upper thresholds for edge detection
        edges = cv2.Canny(gray, 100, 270)
    elif method == "roberts":
        # Apply Roberts cross operator
        kernel = np.array([[1, 0], [0, -1]], dtype=np.float32)  # Define Roberts cross kernel
        edges = cv2.filter2D(gray, -1, kernel)  # Apply the kernel to the image
        edges = np.uint8(np.absolute(edges))  # Convert to absolute values and 8-bit unsigned integer

    # Find contours for object counting
    # RETR_EXTERNAL retrieves only the extreme outer contours
    # CHAIN_APPROX_SIMPLE compresses horizontal, vertical, and diagonal segments
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    object_count = len(contours)  # Count the number of contours (objects)

    # Convert edges back to Pygame surface
    edge_surface = pygame.surfarray.make_surface(np.fliplr(np.rot90(edges)))  # Convert back to Pygame surface
    return edge_surface, object_count  # Return the processed image and object count