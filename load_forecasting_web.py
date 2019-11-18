from flask import Flask, request 
from joblib import load
import pandas as pd
import numpy as np

#create Flask app
app = Flask(__name__) 


def load_model():

   global model
   #Load Random Forest Regressor model
   model = load('load_forecasting_model_v010.joblib')



@app.route('/forecast')
def forecast():
  #get values from url
   HT1 = request.args.get('HT1') 
   HT2 = request.args.get('HT2') 
   HT3 = request.args.get('HT3') 
   HT4 = request.args.get('HT4') 
   HT7 = request.args.get('HT7') 
   HT8 = request.args.get('HT8') 
   HT9 = request.args.get('HT9')
   Hour = request.args.get('Hour') 
   BusinessHour = request.args.get('BusinessHour')
   Daytype = request.args.get('Daytype') 
   Day = request.args.get('Day') 
   Months = request.args.get('Months')
  
  #create dataframe to pass it in model
   df =pd.DataFrame()
   df['HT1'] = [HT1]
   df['HT2'] = [HT2]
   df['HT3'] = [HT3]
   df['HT4'] = [HT4]
   df['HT7'] = [HT7]
   df['HT8'] = [HT8]
   df['HT9'] = [HT9]
   df['Hour'] = [Hour]
   df['BusinessHour'] = [BusinessHour]
   df['Daytype'] = [Daytype]
   df['Day'] = [Day]
   df['Months'] = [Months]

   prediction = model.predict(df)
   
   #y is computed  y=np.log1p(df_60min['Appliances']).  (np.expm1 inverse of np.log1p)
   return '''<h1>The predicted consumption of appliances is: {}</h1>'''.format(np.expm1(prediction))



if __name__ == '__main__':
   try:
       load_model()
       print("Model loaded")

   except Exception as e:
       print("Loading of model was failed")
       print(str(e))
   #run app in debug mode on port 9181    
   app.run(port=9181,debug=True) 