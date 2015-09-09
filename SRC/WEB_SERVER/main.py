"""Flask demo"""
from flask import Flask, render_template, request
import json
import sys
sys.path.append('../PREDICTOR')
from satisfcation_predictor import Predictor

# Init Flas app and Twitter api
app = Flask(__name__)

predictor = None

@app.route('/')
def index():
    return render_template('/index.html')


@app.route('/show', methods=['GET', 'POST'])
def show_tweets():
    reviewText = request.form['screen_name'].encode('ascii', 'ignore').lower().strip()
    try:
        print "Review text is ", reviewText
	answer = predictor.predict(reviewText)
	print answer
    except Exception as e:
   	print 'Some error', reviewText, "\n", str(e) 
    else:
    	pass
        # Never a bad idea to save your data - you're a data scientist after all!
#        with open('tweets/%s.json' % user, 'w') as f:
#           json.dump(raw_tweets, f, indent=2)

        # parse raw tweets into something you want to display
#tweets = [
#           tweet.get('user', {}).get('name', 'Unknown tweeter') + ': ' +
#           tweet.get('text', '(no text)')
#           for tweet in raw_tweets]

    return render_template('/index.html', answer=answer)


if __name__ == '__main__':
    predictor = Predictor()
    #app.run(debug=True, port=5000)
    app.run(host='0.0.0.0', debug=True)  # Never have debug = True when hosting a public website!
