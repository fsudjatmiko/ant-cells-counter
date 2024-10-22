# Ant and Cells Counter with GUI

This project is a graphical user interface (GUI) for performing edge detection on images using the Pygame library. Users can select an image and choose between Canny or Roberts edge detection methods, then view the processed image along with an object count.

## Important (For Learning)
I've put every line explaination in the edge detection code for learning purposes.

## Features
- **Image Selection**: Users can select an image from the `images` folder.
- **Edge Detection**: Supports Canny and Roberts edge detection methods.
- **Object Counting**: Displays the number of detected objects after processing.
- **Retry or Quit**: After viewing the processed image, users can choose to retry with a new image or quit the application.

## Requirements
- Python 3.x
- Pygame
- OpenCV (cv2)
- NumPy

## Setup

1. Clone the repository and navigate to the project folder:
    ```bash
    git clone https://github.com/mikrll/ant-cells-counter.git
    cd edge-detection-gui
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use: .venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Place your images in the `images` folder. (I put 2 example images)

5. Run the application:
    ```bash
    python src/main.py
    ```


## Usage
1. Run the program using `python src/main.py`.
2. Select an image from the list.
3. Choose an edge detection method (Canny or Roberts).
4. View the processed image and object count.
5. Select **Retry** to process another image, or **Quit** to exit.

## Example Images
Place your images of ants or microscopic cells in the `images/` folder to analyze and process them.

## Contributing
Feel free to submit issues or create pull requests. Contributions are welcome!

