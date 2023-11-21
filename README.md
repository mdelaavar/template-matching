# Template Matching Project
Detect and visualize instances of a template image in a collection of target images using template matching in Python with OpenCV.
# Overview
This project focuses on template matching, a computer vision technique that allows the identification of a specific template within larger images. The primary goal is to detect instances of a given template image in a collection of target images and visualize the results. The project is implemented in Python using the OpenCV library.

# Features
Template Matching Methods: The code supports various template matching methods, including cv2.TM_SQDIFF and cv2.TM_SQDIFF_NORMED. You can uncomment other methods in the code as needed and experiment with their effectiveness.

Thresholding: The implementation includes thresholding to filter out matches based on a predefined threshold value. The threshold can be adjusted depending on the chosen template matching method.

Folder Organization: Detected matches are organized into folders based on the chosen template matching method. Each folder contains images that have matches in the corresponding method.

# How to Use
Install Dependencies:

Make sure you have Python and the OpenCV library installed.
Prepare Template and Target Images:

Place your template image (phone.jpg in the provided example) in the images directory.
Add target images to the images directory.
Run the Code:

Execute the Python script in your terminal or preferred Python environment.
Results:

Detected matches will be displayed with rectangles around the matched regions.
Processed images will be saved in folders corresponding to the template matching method used.
# Customization
Template Image: You can easily replace the template image (phone.jpg) with your own template image.

Template Matching Methods: Experiment with different template matching methods by uncommenting the desired methods in the code.

Threshold Adjustment: Modify the threshold value to fine-tune the matching results for different methods.

# Notes
The code is designed to be a template and can be extended for specific use cases or integrated into larger projects.

Feel free to explore other OpenCV functionalities or computer vision techniques to enhance the project.

# Acknowledgments
This project utilizes the OpenCV library, an open-source computer vision and machine learning software library.
