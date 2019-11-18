# Predicting Energy Consumption

Based on data provided by Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/Appliances+energy+prediction), we try to predict consumption of appliances using a Random Forest Regressor model via a Web API.

In order to fullfil assignment's requirements, I create an API load_forecasting_web.py which someone could call using a specific URL.

However, I also created a Dash Framework which i recommend to check too.

Below description is referred in both APIs.



## Installation

Before running APIs, you have to install packages of the requirements.txt.

```shell
$ for /f %i in (requirements.txt) do conda install -c conda-forge --yes %i
$ pip install meteocalc
$ pip install scikit-learn
```


## Usage
To run the Dash API application, use the command

```shell
$ python path\dash_app.py
 * Serving Flask app "dash_app" (lazy loading)
 * Environment: production   Use a production WSGI server instead.
 * Debug mode: on
Running on http://127.0.0.1:9181/
Debugger PIN: 143-319-046
```

To run the Flask API application, use the command

```shell
$ python path\load_forecasting_web.py
 * Serving Flask app "dash_app" (lazy loading)
 * Environment: production   Use a production WSGI server instead.
 * Debug mode: on
Running on http://127.0.0.1:9181/
Debugger PIN: 143-319-046
```


## Documentation

As our web service is up and running, call the API using a browser.

For the Dash framework call: http://127.0.0.1:9181/

For the Flask API call: http://127.0.0.1:9181/forecast?HT1=12&HT2=15&HT3=13&HT4=16&HT7=17&HT8=15&HT9=18&Hour=15&BusinessHour=1&Daytype=1&Day=13&Months=7

### Break down into end to end API

This implemantation was created in order to predict energy consumption of a house. A Random Forest Regressor model was trained and saved at file load_forecasting_model_v010.joblib
and is used by the API.

Using the specific URL, user will retrieve the prediction of  energy consumption (Wh) in an hour.

Dash framework is user friendly and provide an interface to perform tests more easily.

Specifically, user has to complete the below parameters:

HT1 - feels like temperature in kitchen area, in Celsius
HT2 - feels like temperature in living room area, in Celsius
HT3 - feels like temperature in laundry room area, in Celsius
HT4 - feels like temperature in office room, in Celsius
HT7 - feels like temperature in ironing room, in Celsius
HT8 - feels like temperature in teenager room, in Celsius
HT9 - feels like temperature in parents room, in Celsius
Hour of day - LOV (0-23)
BusinessHour - LOV (1,0) - 1 between '09:00:00' and '17:00:00' else 0
Daytype - LOV (1,0) - 1 weekday, 0 weekend
Day of month -LOV (1,31)
Month - LOV (1,12)



##Give an example

Giving the below values in parameters

HT1=12
HT2=15
HT3=13
HT4=16 
HT7=17 
HT8=15 
HT9=18 
Hour=15 
BusinessHour=1 
Daytype=1
Day of month=13 
Month=7

result:
The predicted consuption of appliances is: "[80.80237926]"
