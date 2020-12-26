# A Facial Sentiment Analysis Journey: From Scraping Your First Image to a Stable Model
<p align="center">
  <img width="640" height="360" src="https://miro.medium.com/max/640/1*tLpUlxNvKeXh8XUEvaCGPQ.gif"><br>
  <i>Now everybody around me knows what a sentiment analysis is 😄️</i>
</p>
My intention here is not to present you one of those shiny tutorials but an organic & imperfect journey that I had with unsuccessful Keras models, wrongly tagged stock photos & treacherous Scrapy codes! We have three parts here in total. Let me summarise them for the tl;dr crowd:<br>

* **Part 1:** With just 180 images per class, we are going to create a baseline model with (and without) Image Data Generator module and see the outcome.<br>
* **Part 2:** We are going to loot… \*cough\* I mean, collect thousands of images with Scrapy and discuss why Pikachu seems impeccably happy all the time!<br>
* **Part 3:** Unveil some of the toolkit to fine-tune our models and prepare the platform to use our pretrained model file and implement it to our webcam.<br>
## [Let's dive in to this Medium article!](https://gulmert89.medium.com/facial-sentiment-analysis-by-using-scrapy-and-keras-9d8c20246895)

---
Before you go, let me clarify some of the files above:<br>
* [first_model.ipynb](https://github.com/gulmert89/projects/blob/main/facial_sentiment_analysis/first_model.ipynb): The model trials with 180 images. This is also the introduction of the project.
* [second_model.ipynb](https://github.com/gulmert89/projects/blob/main/facial_sentiment_analysis/second_model.ipynb): The trials with 180 real + 1000 generated images. An image generation step was added.
* [third_model.ipynb](https://github.com/gulmert89/projects/blob/main/facial_sentiment_analysis/third_model.ipynb): The trials with lots of images! Also we fine-tuned the model here with various Keras callbacks.
* [scraped_jsons_to_imgs.ipynb](https://github.com/gulmert89/projects/blob/main/facial_sentiment_analysis/scraped_jsons_to_imgs.ipynb): We collected thousands of image links with Scrapy. They had to be converted to images.
* [video_capture.ipynb](https://github.com/gulmert89/projects/blob/main/facial_sentiment_analysis/video_capture.ipynb): Preparation of the pretrained model file. It's implemented to our webcam.
