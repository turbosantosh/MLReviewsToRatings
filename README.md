# Ratings Predictor

## Zocdoc Potential ratings for reviews

@Author: Santosh Sonawane 

### NOTE:
I am no more maintaining this repo. Please feel free to use and send PR if you have any improvements. 
     This project was done as a part of a Machine Learning course that I attended at General Assembly, NY.
https://github.com/ga-students/DAT-23-NYC 


This project explores different machine learning techniques to predict if a user is satisfied given his review comments. 
Assumption: If a user rates 4,5 then he is satisfied.

Data is fetched by scraping zocdoc.com for all the Primary care physicians in Manhattan.

## Requires
1. BeautifulSoup Dom parser, if you want to use the extractor/scraper
2. pickle
3. scikit (Anaconda)
4. flask

## How to run:
1. cd SRC/WEB_SERVER
2. python main.py
It will train the machine learning model using the zocdoc files in DATA and start a flask webserver.

## Directory Structure:
* README.md - Self.
* DATA 
       Data stored as DocName,DocDegree,Location,PatientName,ReviewDate,OverallRating,BedsideMannerRating,WaitTimeRating,Review
    * zocdoc2.csv 112,000 thousand records 
    * train.csv 60,000 records
    * test.csv 52,000 records
* SRC
       Python and iPython source code
    * There are following components as of now:
    	WebScrapper - Scrapes zocdoc.com and stores all doctors HTML.
	HTMLExtractor - Extracts and cleans up information from the HTMLs and stores in the CSV format
	AnalyzerAndPredictor - Analyzes the data for insights and Has models for predicting ratings from reviews.
    * web_scrapper.py Provides general APIs for scraping the web.
    * zoc_docscrapper.py Uses web_scrapper.py to fetch all Doctors pages as HTMLs
    * html_extractor.py Provides APIs for general extraction data extraction from HTML
    * doctor_reviews_extractor.py Uses html_extractor.py to extract the data and stores in the CSV format
    * data_analysis_and_predictions.ipynb Ipython Notebook that runs through the data and Implements Logistic Regression topredict is a user is satisfied or not
       Data set is skewed towards Positives-91% positives, so Accuracy and Recall are not the best metrics. 
       Accuracy, Precision and Recall tested using cross validation and input test set resulted in ~99% accuracy.

## Enhancements:
* Try other classifiers
* Use tfid vectorizer and trigrams. Try increasing number of Features
* Use Dimensionality reduction to reduce the features
* Try multiclassification techniques to predict ratings as numbers
* Try Polynomial Features to predict numbers as continuous values (This model is too slow)
* Develop a web interface and web server that will take user text and predict his happiness
* See how does this model apply to YELP review, where users give ratings between 1-5
* To quantify user reviews. We can potentially scrape blogs of people regarding some doctor and say what would they rate this doctor as
