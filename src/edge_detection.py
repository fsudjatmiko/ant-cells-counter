import cv2  
import numpy as np  
import pygame  

def apply_edge_detection(image, method):
    image_array = pygame.surfarray.array3d(image) 
    image_array = np.rot90(image_array)  
    image_array = np.fliplr(image_array)  
    gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY) 

    if method == "canny":
        edges = cv2.Canny(gray, 100, 270)

    elif method == "roberts":
        kernel = np.array([[1, 0], [0, -1]], dtype=np.float32)  
        edges = cv2.filter2D(gray, -1, kernel)  
        edges = np.uint8(np.absolute(edges))  

    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    object_count = len(contours)  

    edge_surface = pygame.surfarray.make_surface(np.fliplr(np.rot90(edges)))  
    return edge_surface, object_count  