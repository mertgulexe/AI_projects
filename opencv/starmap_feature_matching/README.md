# Feature Matching Study on a StarMap
For over a few weeks, I have been planning to study object detection deeply but I didn't know what would make me start...<br>...aand here it is!
<p align="center">
  <i>Do you know where these little guys locate?</i><br>
  <img width="114" height="114" src="https://github.com/gulmert89/projects/blob/main/opencv/starmap_feature_matching/Small_area.png">
  <img width="154" height="154" src="https://github.com/gulmert89/projects/blob/main/opencv/starmap_feature_matching/Small_area_rotated.png"><br>
  <i>Here they are!</i><br>
  <img width="800" height="528" src="https://github.com/gulmert89/projects/blob/main/opencv/starmap_feature_matching/StarMapMarked.png"><br> 
</p>

I think you got the idea here :) It's quite easy to locate the position of a plain template taken from an image (here, it's the smaller frame at top right) but the problem arises when the template is zoomed, flipped and/or rotated etc. Certainly, there are multiple options to come up with a solution, and I used some pure Python skills to find its location _roughly_. However, **OpenCV** will come to our rescue and find its exact location!<br>

**Files:**<br>
* For the initial study, please see the [notebook](https://github.com/gulmert89/projects/blob/main/starmap_feature_matching/starmap_notebook.ipynb) file. This will be the main file of the project and it can be followed to see the progress.<br>
* The modules that you will [require](https://github.com/gulmert89/projects/blob/main/starmap_feature_matching/requirements.txt) to use the notebook. The script only needs  **numpy** & **opencv-python** at the moment.<br>
