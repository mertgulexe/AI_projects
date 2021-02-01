print("""To find the location of a template in the bigger picture, please provide two images.
You also can use the default images by just pressing enter:
Template    : 'Small_area.png'
Big Picture : 'StarMap.png'\n""")

import cv2
import numpy as np

def main():
    smaller_name = input("Please enter the name of the smaller image : ") or "Small_area.png"
    bigger_name = input("Please enter the name of the bigger image  : ") or "StarMap.png"

    smaller_img = cv2.imread(smaller_name)
    big_picture = cv2.imread(bigger_name, 
                             cv2.IMREAD_IGNORE_ORIENTATION | cv2.IMREAD_COLOR)

    smaller_img_gray = cv2.imread(smaller_name, 0)
    big_picture_gray = cv2.imread(bigger_name, 0)

    HEIGHT, WIDTH = smaller_img_gray.shape

    result = cv2.matchTemplate(image=big_picture_gray, 
                            templ=smaller_img_gray, 
                            method=cv2.TM_SQDIFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    (startX, startY) = min_loc    # top left corner
    (endX, endY) = (startX + WIDTH, startY + HEIGHT)    # bottom right corner

    def mark_the_bigPicture(modified_image_name="StarMapMarked.png"):
        """This function creates a rectangle over the template found in the 
        bigger picture and shows the coordinates of the corner points.
        The only variable it takes is the modified image name as a string."""
        # yellow rectangle
        cv2.rectangle(img=big_picture, 
                    pt1=(startX, startY), 
                    pt2=(endX, endY), 
                    color=(0, 255, 255), 
                    thickness=2)

        # TEXT & ORIGIN of top left/right and bottom left/right points
        text_TL = f"({startX}, {startY})"
        text_TR = f"({startX + WIDTH}, {startY})"
        text_BL = f"({startX}, {startY + HEIGHT})"
        text_BR = f"({startX + WIDTH}, {startY + HEIGHT})"
        org_TL = (startX-130, startY-5)
        org_TR = (startX+WIDTH+10, startY-5)
        org_BL = (startX-130, startY+HEIGHT+10)
        org_BR = (startX+WIDTH+10, startY+HEIGHT+10)

        for TEXT, ORIGIN in zip((text_TL, text_TR, text_BL, text_BR), 
                                (org_TL, org_TR, org_BL, org_BR)):
            # texts for the corner points in (X,Y) format
            cv2.putText(img=big_picture, 
                        text=TEXT, 
                        org=ORIGIN, 
                        fontFace=cv2.FONT_HERSHEY_COMPLEX, 
                        lineType=cv2.LINE_AA,
                        fontScale=0.7, 
                        color=(0,255,0), 
                        thickness=1)
        cv2.imwrite(modified_image_name, big_picture)
        return modified_image_name

    marked_bigPicture = mark_the_bigPicture()

    # to display it in a window
    marked_bigPicture = cv2.imread(marked_bigPicture)
    cv2.namedWindow("StarMap_window", cv2.WINDOW_NORMAL)
    cv2.imshow("StarMap_window", marked_bigPicture)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()