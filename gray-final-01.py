'''
this code exe. truly in grayscale but problems are:
1- accuracy is not good (it finds "telephone" template in all images
2- after finding the template in a image it should add that to its method's folder but
know it doesn't have this command
3- the code doesn't work with color images and have problem if provided with colors
'''

import numpy as np
import cv2
import glob
import os

template = cv2.imread('images/phone.jpg', 0)
h, w = template.shape

methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
name_meth = {"0":"TM_SQDIFF", "1" : "TM_SQDIFF_NORMED", "2" : "TM_CCORR",
             "3" : "TM_CCORR_NORMED", "4" : "TM_CCOEFF", "5" : "TM_CCOEFF_NORMED" }

for image in os.listdir("images/"):
    img = cv2.imread(os.path.join("images", image), 0)
    for method in methods:
        img2 = img.copy()
        name = name_meth.get(str(method))
        result = cv2.matchTemplate(img2, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        match_found = False
        threshold = 0.8
        folder_name = name_meth.get(str(method))
        here_path = os.getcwd()
        if name not in os.listdir(here_path):
            os.mkdir(folder_name)

        if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
            location = min_loc
            match_found = min_val < threshold

        else:
            location = max_loc
            match_found = max_val > threshold


        if match_found:
            os.path.join(folder_name, str(image))

        bottom_right = (location[0] + w, location[1] + h)
        cv2.rectangle(img2, location, bottom_right, 255, 2)
        cv2.imshow(name, img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()



