import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import numpy as np
from joblib import load
import pandas as pd
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']


app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


app.layout = html.Div(children=[
    html.H1(children='Prediction Energy Consumption'),
    html.Div(children='''
        A web application framework for Prediction Energy Consumption.
    '''),
    dcc.Input(id='HT1', value='HT1', type='float'),
    dcc.Input(id='HT2', value='HT2', type='float'),
    dcc.Input(id='HT3', value='HT3', type='float'),
    dcc.Input(id='HT4', value='HT4', type='float'),
    dcc.Input(id='HT7', value='HT7', type='float'),
    dcc.Input(id='HT8', value='HT8', type='float'),
    dcc.Input(id='HT9', value='HT9', type='float'),
    dcc.Input(id='Hour', value='Hour', type='float'),
    dcc.Input(id='BusinessHour', value='BusinessHour', type='float'),
    dcc.Input(id='Daytype', value='Daytype', type='float'),
    dcc.Input(id='Day', value='Day', type='float'),
    dcc.Input(id='Months', value='Months', type='float'),
    html.Div(id='my-div'),
    html.Div(children='''
        HT1 - feels like temperature in kitchen area, in Celsius 
    '''),
    html.Div(children='''
        HT2 - feels like temperature in living room area, in Celsius
    '''),
     html.Div(children='''
        HT3 - feels like temperature  in laundry room area, in Celsius
    '''),
      html.Div(children='''
        HT4 - feels like temperature in office room, in Celsius
    '''),
       html.Div(children='''
        HT7 - feels like temperature in ironing room, in Celsius
    '''),
        html.Div(children='''
        HT8 - feels like temperature in teenager room, in Celsius
    '''),
         html.Div(children='''
        HT9 - feels like temperature  in parents room, in Celsius
    '''),
         html.Div(children='''
        Hour of day - LOV (0-23)
    '''),
          html.Div(children='''
        BusinessHour - LOV (1,0) - 1  between '09:00:00' and '17:00:00' else 0
    '''),
          html.Div(children='''
        Daytype - LOV (1,0) - 1 weekday, 0 weekend
    '''),
          html.Div(children='''
        Day of month -LOV (1,31)
    '''),
          html.Div(children='''
        Month - LOV (1,12)
    ''')
])


@app.callback(
    Output(component_id='my-div', component_property='children'),
    [Input(component_id='HT1', component_property='value'),
     Input(component_id='HT2', component_property='value'),
     Input(component_id='HT3', component_property='value'),
     Input(component_id='HT4', component_property='value'),
     Input(component_id='HT7', component_property='value'),
     Input(component_id='HT8', component_property='value'),
     Input(component_id='HT9', component_property='value'),
     Input(component_id='Hour', component_property='value'),
     Input(component_id='BusinessHour', component_property='value'),
     Input(component_id='Daytype', component_property='value'),
     Input(component_id='Day', component_property='value'),
     Input(component_id='Months', component_property='value')]
)
def forecast(HT1,HT2,HT3,HT4,HT7,HT8,HT9,Hour,BusinessHour,Daytype,Day,Months):

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
    return 'The predicted consuption of appliances is: "{}"'.format(np.expm1(prediction))


if __name__ == '__main__':
    from joblib import dump, load
    model = load("load_forecasting_model_v010.joblib")
    app.run_server(port=9181,debug=True)
