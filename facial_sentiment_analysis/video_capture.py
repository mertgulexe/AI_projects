import cv2
import numpy as np
from cvlib import detect_face
from keras.models import load_model
from PIL.Image import open as Image_open

best_model_path = "best_model.h5"
model = load_model(best_model_path)

def getClassName(classIndex):
    "A basic function to get the class name."
    if classIndex==3:   return "Happy"    
    elif classIndex==1: return "Sad"    
    elif classIndex==2: return "Shocked"
    else:               return "Poker Face"

cap = cv2.VideoCapture(0)

detectFace_threshold = 0.80
predictFace_threshold = 0.40 * 100

try:
    while cap.isOpened():

        ret, frame = cap.read()
        if not ret:
            print("Can't receive the frame.")
            break
        
        faces, confidences = detect_face(frame, threshold=detectFace_threshold)
        for f in faces: 
            (startX, startY) = (f[0], f[1])
            (endX, endY) = (f[2], f[3])
            cropped_frame = np.copy(frame[startY:endY, startX:endX])
            if (cropped_frame.shape[0]) < 10 or (cropped_frame.shape[1]) < 10:
                continue

            cropped_frame = cv2.resize(cropped_frame, (64,64))        
            cropped_frame = cv2.cvtColor(cropped_frame, code=6)
            cropped_frame = cropped_frame.astype("float32") / 255.0
            cropped_frame = np.expand_dims(cropped_frame, axis=[0,3])
            confidences = model.predict(cropped_frame)[0]
            max_probability = max(confidences)*100
            classIndex = np.argmax(confidences)
            className = getClassName(classIndex)

            if max_probability > predictFace_threshold:
                frame_text = f"{className} ({int(max_probability)}%)"
                if className == "Shocked":
                    rect_color = text_color = (0, 255, 255)
                elif className == "Sad":
                    rect_color = text_color = (255, 0, 0)
                elif className == "Happy":
                    rect_color = text_color = (0, 255, 0)
                elif className == "Poker Face":
                    rect_color = text_color = (214, 112, 218)
            else:
                rect_color = text_color = (0, 0, 255)
                frame_text = "Reading..."    

            cv2.rectangle(img=frame, 
                          pt1=(startX, startY), 
                          pt2=(endX, endY), 
                          color=rect_color, 
                          thickness=2)

            startY = startY - 10 if startY - 10 > 10 else startY + 10
            cv2.putText(img=frame, 
                        text=frame_text, 
                        org=(startX, startY), 
                        fontFace=cv2.FONT_HERSHEY_COMPLEX, 
                        lineType=cv2.LINE_AA,
                        fontScale=0.6, 
                        color=text_color, 
                        thickness=1)

        cv2.imshow("Face_Sentiment", frame)
        if cv2.waitKey(1) > 0:
            break

    cap.release()
    cv2.destroyWindow("Face_Sentiment")
except:
    cap.release()
    cv2.destroyAllWindows()