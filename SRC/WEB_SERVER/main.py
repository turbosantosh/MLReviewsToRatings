"""Flask demo"""
from flask import Flask, render_template, request
import json
import sys
sys.path.append('../PREDICTOR')
from satisfcation_predictor import Predictor

app = Flask(__name__)
app._static_folder = "./static/"
predictor = None

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/show', methods=['GET', 'POST'])
def show_tweets():
    reviewText = request.form['screen_name'].encode('ascii', 'ignore').lower().strip()
    print reviewText
    try:
	print "Review text is ", reviewText
	answer = predictor.predict(reviewText)
	print answer
    except Exception as e:
   	print 'Some error', reviewText, "\n", str(e) 
    else:
    	pass

    return render_template('/index.html', answer=answer, previous_text=reviewText)


if __name__ == '__main__':
    predictor = Predictor()
    app.run(host='0.0.0.0', debug=False)  # Never have debug = True when hosting a public website!
