from tensorflow.keras.models import load_model
from streamlit import image as st_image, title as st_title, cache as st_cache,\
    button as st_button, text as st_text, file_uploader as st_file_uploader
from cv2 import VideoCapture, resize, cvtColor, rectangle, putText, imwrite,\
    imshow, imread, destroyAllWindows, FONT_HERSHEY_COMPLEX, LINE_AA, waitKey
from numpy import copy, expand_dims, argmax, array
from cvlib import detect_face
from PIL import Image, ExifTags

model = load_model(r'./model/')

st_title("Facial Sentiment Analysis")

def getClassName(classIndex):
    "A basic function to get the class name."
    if classIndex==3:   return "Happy"    
    elif classIndex==1: return "Sad"    
    elif classIndex==2: return "Shocked"
    else:               return "Poker Face"

if __name__ == "__main__":    
    detectFace_threshold = 0.70
    predictFace_threshold = 0.35 * 100
    image_file = st_file_uploader("Upload your selfie here:", type=["jpg", "jpeg", "png"])
    st_text("Hint: Try not to hold the camera too close to your face.")
    if image_file is not None:
        image_file = Image.open(image_file)
        try:
            for orientation in ExifTags.TAGS.keys():
                if ExifTags.TAGS[orientation]=='Orientation':
                    exif_orientation = orientation
                    break        
            exif = image_file._getexif()
            if exif[exif_orientation] == 3:
                image_file = image_file.rotate(180, expand=True)
            elif exif[exif_orientation] == 6:
                image_file = image_file.rotate(270, expand=True)
            elif exif[exif_orientation] == 8:
                image_file = image_file.rotate(90, expand=True)
        except (AttributeError, KeyError, IndexError):
            pass
        frame = array(image_file)        
        height = 370
        width = int((frame.shape[0] / frame.shape[1]) * height)
        frame = resize(frame, (height, width))
        faces, confidences = detect_face(frame, threshold=detectFace_threshold)
        for f in faces:
            # corner points of facial frame: 
            (startX, startY) = (f[0], f[1])    # top left corner
            (endX, endY) = (f[2], f[3])    # bottom right corner
            # crop it from the whole frame:
            cropped_frame = copy(frame[startY:endY, startX:endX])        
            # skip too small frames (10x10 pixels)
            if (cropped_frame.shape[0]) < 10 or (cropped_frame.shape[1]) < 10:
                continue
            # preprocessing on the cropped frame
            cropped_frame = resize(cropped_frame, (64,64))        
            cropped_frame = cvtColor(cropped_frame, code=6)    # convert to grayscale
            cropped_frame = cropped_frame.astype("float32") / 255.0
            cropped_frame = expand_dims(cropped_frame, axis=[0,3])
            confidences = model.predict(cropped_frame)[0]    # probability value
            max_probability = max(confidences)*100
            classIndex = argmax(confidences)
            className = getClassName(classIndex)

            if max_probability > predictFace_threshold:
                frame_text = f"{className} ({int(max_probability)}%)"
                # BLUE - GREEN - RED
                if className == "Shocked":
                    rect_color = text_color = (255, 255, 0)
                elif className == "Sad":
                    rect_color = text_color = (0, 255, 255)
                elif className == "Happy":
                    rect_color = text_color = (0, 255, 0)
                elif className == "Poker Face":
                    rect_color = text_color = (218, 112, 214)

            else:
                rect_color = text_color = (255, 0, 0)
                frame_text = "Reading..."    

            rectangle(img=frame, 
                        pt1=(startX, startY), 
                        pt2=(endX, endY), 
                        color=rect_color, 
                        thickness=2)

            # let's keep the text in the frame and avoid edges:
            startY = startY - 10 if startY - 10 > 10 else startY + 10
            putText(img=frame, 
                        text=frame_text, 
                        org=(startX, startY), 
                        fontFace=FONT_HERSHEY_COMPLEX, 
                        lineType=LINE_AA,
                        fontScale=0.6, 
                        color=text_color, 
                        thickness=1)

        st_image(frame)