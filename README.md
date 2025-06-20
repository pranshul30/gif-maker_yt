# Python GIF Maker with Imageio v3

## 🚀 Overview

Welcome to the **Python GIF Maker** project! This simple yet powerful tool demonstrates how to create captivating animated GIFs from a series of images using the latest version of the `imageio` library (v3+).

Whether you're a Python beginner looking to understand image manipulation or an experienced developer eager to explore `imageio v3`'s capabilities, this project offers a clear, concise, and easy-to-follow example. Transform your static image sequences into dynamic animations with just a few lines of code!

## ✨ Features

* **Simple & Intuitive:** Easy to understand and modify code.
* **Imageio v3 Powered:** Leverages the modern `imageio` library for efficient GIF creation.
* **Customizable:** Easily adjust GIF duration, loop count, and input/output paths.
* **Educational:** A great starting point for learning about image processing and animation in Python.

## 🌟 What You'll Learn

* How to install and set up the `imageio` library.
* Reading multiple image files (e.g., `.png`, `.jpg`) programmatically.
* Generating high-quality animated GIFs from an image sequence.
* Basic concepts of `imageio` for multimedia file handling.

## 🛠️ Installation

Before you begin, ensure you have Python 3.7+ installed on your system.

1.  **Clone the repository (or download the project files):**
    ```bash
    git clone [https://github.com/your-username/your-gif-maker-project.git](https://github.com/your-username/your-gif-maker-project.git)
    cd your-gif-maker-project
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    * **Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
    * **macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

4.  **Install the required libraries:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Make sure you have a `requirements.txt` file with `imageio` listed, e.g., `imageio>=3.0.0`)*

## 🚀 How to Use

1.  **Prepare your images:**
    Place the images you want to convert into a GIF in a designated folder. Ensure they are sequentially named (e.g., `frame_001.png`, `frame_002.png`, `frame_003.png`, or `image1.jpg`, `image2.jpg`, etc.) for easy processing.

2.  **Update the script (if necessary):**
    Open `gif_maker.py` (or whatever you name your main script) and adjust the `input_image_path`, `output_gif_path`, and `duration_per_frame` variables as needed.

    ```python
    # Example snippet from your script import imageio.v3 as iio

        file=['1.png','2.png'] 
        images=[ ]

        for i in file:
        images.append(iio.imread(i))
  
    iio.imwrite('3.gif',images,duration=200,loop=0)  
    
    duration_per_frame_seconds = 0.1 # Duration for each frame in seconds
    loop_count = 0 # 0 means loop forever, 1 for one time, etc.

    # ... rest of your code
    ```
    After running, your generated GIF will be saved in the specified `output_gif_path`.
