## HackerEarth Machine Learning Challenge: Are your employees burning out?
> Oct 21, 2020, 04:00 AM EEST - Nov 20, 2020, 04:00 AM EET
<p align="center">
  <img width="910" height="410" src="https://media-fastly.hackerearth.com/media/hackathon/hackerearth-machine-learning-challenge-predict-burnout-rate/images/8beab99412-Burnout_Cover_Image.png"><br>
  <i>Source: <a href="https://www.hackerearth.com/challenges/competitive/hackerearth-machine-learning-challenge-predict-burnout-rate/">HackerEarth</a></i>
</p>

## The main goal here was to estimate the <i>Burn Out</i> rate of the employees.<br>
Yep, this was a regression problem with a few important features. I wanted to write the notebook as a tutorial to myself to go over the basics of such problems and followed these steps:<br>
* Import the essential modules and the dataset (duh!).
* Check out the NaN and unique values and also the value types.
* Perform one-hot encoding if necessary to make things easier for the models.
  * ...because there are a couple of binary features as well as some discrete & continuous ones.
* Modify the features to get some useful information out of them.
  * Feature engineering, e.g how about we inspect WFH option by gender?
* Fill in the blanks (NaNs) with proper values.
  * Though we might just get rid of them as well.
* Create a baseline model to see where we are.
* Try different models (with different features) and tune their hyperparameters
* Dance with the best model till sunrise.
---

## "I could have done better."
This was the first "active" hackathon that I attended individually. Managed to enter the first 10%, which is a _good-enough_ success for me, but I could have been in the first 50. 
Just the day after the deadline, I came up with an idea _(linearization of a feature which exhibits a polynomial behaviour)_ that pulled me up 10 more people _(48th place)_.<br>
In this notebook ([burning_out.ipynb](https://github.com/gulmert89/projects/blob/main/burnout_rate/burning_out.ipynb)), I wanted to practice the basics of linear regression models and some other ML tools once again since I mostly focused on deep learning lately. Also I posted it as a [Kaggle notebook](https://www.kaggle.com/gulmert89/a-regression-adventure-up-to-92-98) (why don't you vote it up, please? :smile:) .<br> I really, REALLY wonder with which solution the person in the first place came up, so I... _\*cough\*_ ...emailed and asked him! _\*stalker alert\*_ He sent me his GitHub link and [ktrain](https://github.com/amaiya/ktrain) was the module he used. I also took a look at [his](https://github.com/victorkras2008/HackerEarth-Machine-Learning-Challenge) solution and saw that he started the model with a different learning rate and a different metric. I think at this point, I may or may not give my code another shot (specifically to the deep learning section). Or a wiser idea would be to move forward and to take these into consideration in next projects.<br>

To see the details about the hackathon, see my <code>.ipynb</code> file.
