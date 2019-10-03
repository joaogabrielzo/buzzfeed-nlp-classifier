from flask import Flask,render_template,url_for,request
import pandas as pd
import numpy as np
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.pipeline import Pipeline
from sklearn import svm
from sklearn.metrics import confusion_matrix, f1_score
from sklearn.model_selection import train_test_split, KFold
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
    df_titles = pd.read_csv('clickbait_or_not.csv')

    # Separating feature and label
    X = df_titles['title']
    y = df_titles['label']

    # Transforming the dataset into a matrix of token counts
    cv = CountVectorizer()
    X = cv.fit_transform(X)

    # Assigning the model
    clf = MultinomialNB()
    
    # Separating into training and testin
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 42)
    
    # Fitting the training set
    clf.fit(X_train, y_train)
    clf.score(X_test, y_test)

    # Predicting the input
    if request.method == 'POST':
        message = request.form['message'] # Gets the input (link)
        page = requests.get(message) # Requests access to the link
        soup = BeautifulSoup(page.text, 'html.parser') # Parse the link's html
        text = soup.find('h1').get_text() # Gets the headline (h1)
        data = [text] # Assign to a list
        vect = cv.transform(data).toarray() # Transforms into a token count matrix
        my_prediction = clf.predict(vect) # Predicts
    return render_template('result.html',prediction = my_prediction)



if __name__ == '__main__':
	app.run(debug=True)