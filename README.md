Customer Churn Prediction
The project consists of data from retail superstore across Massachusetts in USA. The chain of superstore is facing high customer churn and as a result there has been reduction in overall sales and hence profit.
In order to reverse the customer churn the store wants to distribute discount coupons to customers whom they thing would not churn. To determine the type of customer that will again buy goods from the store we analyze the demographic of customers and build a model to predict whether a customer will churn or not in future.

Data 
The data structure in the database.

![Retail_ER_diag](https://user-images.githubusercontent.com/40518603/112862186-2351e180-90d3-11eb-9a8d-31101a67e8df.png)

 


The Dashboard of customer demographics
 



Landing Page of App
 

 
Prediction 
The prediction is at the bottom of the screen: The customer will again buy goods from the store

 

Tech Stack
•	Front-End: HTML, CSS, Bootstrap
•	Back-End: Flask
•	IDE: Jupyter notebook, Pycharm

How to run this app
•	First create a virtual environment by using this command:
•	conda create -n myenv python=3.6
•	Activate the environment using the below command:
•	conda activate myenv
•	Then install all the packages by using the following command
•	pip install -r requirements.txt
•	Now for the final step. Run the app
•	python app.py

Workflow
Data Collection
The customer survey data was initially handwritten in a piece of paper. The data is written in excel. The data is uploaded in MySql in the database.
Data Preprocessing
•	As the data has been transferred from survey data to excel incomplete data has been removed during process.
•	Different  joins are created between different tables
•	We create schemas for all tables. One table is the transactional table and the other being Master Tables.
•	Plot bar charts for different tables to analyze the features.
Model Creation
•	Used Logistic regression and found its accuracy and evaluated the prediction through classification metrics such as confusion matrix.
