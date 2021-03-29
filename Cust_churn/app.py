from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.linear_model  import LogisticRegression
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('Cust_Retail_churn_pred_log_model.pkl', 'rb'))
@app.route('/',methods=['GET','POST'])
def Home():
    return render_template('index.html')

standard_to = StandardScaler()
@app.route("/predict", methods=['GET','POST'])
def predict():
    Race_Asians=0
    Race_White=0
    Race_Others=0
    Race_Native_American=0
    my_list = []

    if request.method == 'POST':
        AvgCountItems = float(request.form['AvgCountItems'])
        AvgItemPrice=float(request.form['AvgItemPrice'])
        Trips=float(request.form['Trips'])
        TotalRevenue=float(request.form['TotalRevenue'])
        Cust_Sex = request.form['Cust_Sex']
        if (Cust_Sex == 'Male'):
            Cust_Sex = 1
        else:
            Cust_Sex = 0
        Cust_Income = float(request.form['Cust_Income'])
        Cust_Age = int(request.form['Cust_Age'])
        Cust_Children = int(request.form['Cust_Children'])
        Cust_Rel_Status = request.form['Cust_Rel_Status']
        if (Cust_Rel_Status == 'Unmarried'):
            Cust_Rel_Status = 1
        else:
            Cust_Rel_Status = 0
        Race_Black=request.form['Race_Black']
        if(Race_Black=='Black'):
            Race_Native_American=0
            Race_Asians=0
            Race_White=0
            Race_Others=0
            Race_Black=1
        elif(Race_Black=='White'):
            Race_Native_American = 0
            Race_Asians = 0
            Race_Others = 0
            Race_White = 1
            Race_Black = 0
        elif(Race_Black=='Others'):
            Race_Native_American = 0
            Race_Asians = 0
            Race_Others = 1
            Race_White = 0
            Race_Black = 0
        else:
            Race_Native_American = 1
            Race_Asians = 0
            Race_Others = 0
            Race_White = 0
            Race_Black = 0
        #mylist = [Race_Black, Race_White, Cust_Rel_Status, TotalRevenue, Cust_Children, Trips, AvgItemPrice, Race_Others, AvgCountItems, Race_Native_American, Cust_Income, Cust_Sex, Cust_Age]
        #cols_when_model_builds = model.get_booster().feature_names
        #my_array = np.array(my_list).reshape((1,-1))
        prediction=model.predict([[AvgCountItems, AvgItemPrice, Trips, TotalRevenue, Cust_Sex,Cust_Income,Cust_Age,Cust_Children,Cust_Rel_Status,Race_Black, Race_Native_American, Race_Others, Race_White]])
        #prediction = model.predict(my_array)
        output=int(prediction[0])
        if (output == 0):
            return render_template('index.html',prediction_texts="The Customer will again buy goods from the store")
        else:
            return render_template('index.html',prediction_texts="The Customer will not buy goods from the store next time and will churn")
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

