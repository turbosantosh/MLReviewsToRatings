import pandas as pd
import pickle
import os.path
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.cross_validation import cross_val_score

MODEL_PICKLE_FILE_PATH='../../DATA/modelCurrent.p'
CV_PICKLE_FILE_PATH='../../DATA/cvCurrent.p'

class Predictor():
	_cv = None
	_model = None
        def __init__(self, path='../../DATA/zocdocData2.csv'):
		#Load from the pickle file if it exists
		#Otherwise train the model
		if os.path.isfile(MODEL_PICKLE_FILE_PATH):
			with open(MODEL_PICKLE_FILE_PATH) as f:
				    self._model = pickle.load(f)
				    try:
					    with open(CV_PICKLE_FILE_PATH) as cvp:
						    self._cv = pickle.load(cvp)
						    print 'Loaded the model and cv'
						    return
				    except Exception as e:
					    print "Exception in constructor while loading pickle", str(e)
					    pass
		docData = pd.read_csv(path)
		docData = docData.dropna()
		# Create a feature for isGood
		# Assumption:
		# Reviews Rated 4,5 are good
		# Reviews Rated 1,2,3 are bad
		docData['isGood'] = docData.OverallRating.apply(lambda x: x-3 > 0)
		docData['ReviewWordCount'] = docData['Review'].apply(lambda x: len(x.split()))
		self._cv = TfidfVectorizer(stop_words=['it', 'he', 'she', 'they', 'those', 'that', 'them', 'in', 'on', 'for', 'by', 'of', 'a', 'an', 'the', 'and', 'd', 'that', 'am', 'are', 'I', 'We', 'you'], ngram_range=(1, 3), max_features=20000)
		 #self._cv = TfidfVectorizer(stop_words='english', ngram_range=(1, 3), max_features=10000)
#cv = CountVectorizer(stop_words='english', ngram_range=(1, 3), max_features=5000)
		reviewCV = self._cv.fit_transform(docData.Review)
		self._model = LogisticRegression()
		docDataWReview = reviewCV.toarray()
		X = docDataWReview
		 #print cross_val_score(self._model, X, docData.isGood, cv=5, scoring='roc_auc').mean()
		 #print cross_val_score(self._model, X, docData.isGood, cv=5, scoring='precision').mean()
		self._model.fit(X, docData.isGood)
		with open(MODEL_PICKLE_FILE_PATH, 'w') as f:
			pickle.dump(self._model, f)
		with open(CV_PICKLE_FILE_PATH,'w') as f:
			pickle.dump(self._cv, f)


	def predict(self, review):
		if not self._cv:
			 #self._cv = CountVectorizer(stop_words='english', ngram_range=(1, 3), max_features=5000)
			 #self._cv = TfidfVectorizer(stop_words=['a', 'an', 'the', 'and', 'd', 'that', 'am', 'are', 'I', 'We', 'you'], ngram_range=(1, 3), max_features=20000)
			self._cv = TfidfVectorizer(stop_words=['it', 'he', 'she', 'they', 'those', 'that', 'them', 'in', 'on', 'for', 'by', 'of', 'a', 'an', 'the', 'and', 'd', 'that', 'am', 'are', 'I', 'We', 'you'], ngram_range=(1, 3), max_features=20000)
		X = self._cv.transform([review])
		print "HERER======="
		return self._model.predict(X.toarray())


#Test Driver
def main():
	predictor = Predictor()
	print predictor.predict('This doctor is pretty crazy. I dont like this doctor')
	print predictor.predict('This doctor is pretty wonderful')


if __name__ == "__main__":
        main()
