from flask import Flask,render_template,request

app = Flask(__name__)
import pandas as pd
import numpy as np
import joblib
file = 'static/house_price_prediction1.joblib'
model = joblib.load(file)

@app.route('/',methods=['POST','GET'])
def index():
    if request.method=='GET':
        return render_template('houseprice.html')
    if request.method=='POST':
        bed = int(request.form['bedroom'])
        bath = int(request.form['bathroom'])
        sqftliving = float(request.form['sqftliving'])
        sqftlot = float(request.form['sqftlot'])
        floor = int(request.form['floor'])
        rating = int(request.form['rating'])
        sqftground = float(request.form['sqftground'])
        year = int(request.form['year'])

        data = [[bed,bath,sqftliving,sqftlot,floor,rating,sqftground,year]]
        price = model.predict(data)[0]
        price2 = str(np.round(price,2))
        return render_template('houseprice.html',price=price2)
        

if __name__ == '__main__':
    app.run(debug=True)