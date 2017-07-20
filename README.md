# Shoe Game
General Assembly Final Capstone Project on topic of choice. My choice was the growing culture of athletic sneaker collectors eventually predicting shoe rarity. Using tools and techniques learned in the Data Science Immersive class. Some tools & techniques used are:

Convolutional Neural Networks\
Principal Component Analysis\
Linear Regression\
Logistic Regression\
Support Vector Machines\
Gridsearch\
Ensemble\
Pipelines\
NLP - specifically count, hash, and tf-idf vectorizers\
Hypothesis testing

[My Google Deck](https://docs.google.com/presentation/d/1UOJk8wIvOb7Ah7lUZBQpM79HJMvQfFRcrlScOc5kc74/edit?usp=sharing)

## Process Flow
1. Gathering the raw data
    - Use StockX API
    - Download data into csv to prevent scraping every time

2. Cleaning and Initial Analysis
    - Drop duplicates
    - Take out unnecessary features
    - Convert data types to usable data types
    - Drop null values and non-sensical values

3. Subset data with top 3 brands and perform EDA
    - Section off data to only look at top 3 brands: Nike, Adidas, and Jordan
    - Look at max, min, and mean values
    - Explore data trends in general
    - Perform some hypothesis testing on rarity means

4. Natural Language Processing and Modeling
    - Use count, hash, and tf-idf vectorizers
    - Use every classifier learned in class
    - Use ensemble methods
    - Try to finetune top performing models

5. Clustering
    - Practice clustering using Kmeans
    - Practice clustering using DBSCAN

6. Predict Rarity (regression and classification)
    - Use linear regression
    - Use logistic regression
    - Use pipeline with scaling and principal component analysis

7. Image Processing
    - Use Keras with tensorflow backend to predict if images can predict rare or not
    - Use PICKLE library to convert large image data into actual usable & pullable data
