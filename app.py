# -*- coding: utf-8 -*-
"""
Created on Mon May 24 23:01:59 2021

@author: avi
"""

from flask import Flask,render_template,request
import numpy as np
import pandas as pd
import pickle
app = Flask(__name__)
pickle_in=open('banknote.pkl','rb')
model=pickle.load(pickle_in)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        
        variance=request.form['variance']
        skewness=request.form['skewness']
        curtosis=request.form['curtosis']
        entropy=request.form['entropy']
        prediction=model.predict([[variance,skewness,curtosis,entropy]])
        return 'The predicted value is'+ str(prediction)
        
        
    else:
        return render_template('index1.html')
    




if __name__ == "__main__":
    app.run(debug=True)