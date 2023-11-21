import cv2
import os

template = cv2.imread('images/phone.jpg', 0)
h, w = template.shape

methods = [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
# methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
#            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
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
        threshold = 0.0005  # could be changed foe different method, this value is proper for "SQDIFF_NORMED"
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
            print(os.path.join(folder_name, str(image)))  # make path to the folder of method
            os.chdir(os.path.join(folder_name))  # change directory to save target images in respective folder of method
            image_name = os.path.splitext(image)[0]  # remove extension from end of image name
            filename = image_name + str(method) + ".jpg"
            cv2.imwrite(filename, img2)
            bottom_right = (location[0] + w, location[1] + h)
            cv2.rectangle(img2, location, bottom_right, 255, 2)
            cv2.imshow(name, img2)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            os.chdir('../')   # go back to file.py directory (on level up)