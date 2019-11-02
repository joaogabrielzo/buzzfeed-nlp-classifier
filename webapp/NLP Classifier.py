from flask import Flask,render_template,url_for,request
from sklearn.externals import joblib
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

# Creating the webapp's frontpage
@app.route('/')
def home():
	return render_template('home.html')

# Creating the predicts page
@app.route('/predict',methods=['POST'])
def predict():
    # Loading the trained model
    clf = joblib.load('Naive Bayes Buzzfeed Classifier.pkl')

    # Predicting the input
    if request.method == 'POST':
        message = request.form['message'] # Gets the input (link)
        page = requests.get(message) # Requests access to the link
        soup = BeautifulSoup(page.text, 'html.parser') # Parse the link's html
        text = soup.find('h1').get_text() # Gets the headline (h1)
        data = [text] # Assign to a list
        my_prediction = clf.predict(data) # Predicts
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)