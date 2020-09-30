import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np
import json
import datetime

def create_plot(predictions):
    past_data = pd.read_csv(app.config['PAST_DATA'],index_col=0)
    carbon_saved_dict = {'Cardboard': 0.22, 'Glass': 1.38, 'Metal': 0.10, 'Paper': 0.03, 'Plastic': 0.04}
    scale_kg = [1.1, 1, 5.9, 0.26, 1.8]

    # Create a new dataframe from the new prediction
    top_pred = list(predictions.keys())[0]
    column_for_input = ['Cardboard','Glass','Metal','Paper','Plastic']
    column_for_input_np = np.array(['Cardboard','Glass','Metal','Paper','Plastic'])
    dummy_input = pd.DataFrame(column_for_input_np == top_pred).T
    dummy_input.columns = column_for_input
    dummy_input = dummy_input.astype(int)
    dummy_input['Date'] = datetime.datetime.now().strftime('%Y-%m-%d')
    carbon_saved_dict = {'Cardboard': 0.22, 'Glass': 1.38, 'Metal': 0.10, 'Paper': 0.03, 'Plastic': 0.04}
    colors = ['peru', 'darkturquoise', 'grey', 'dodgerblue', 'red']
    scale_kg = [1.1, 1, 5.9, 0.26, 1.8]
    dummy_input['carbon_footprint_reduce(kg)'] = dummy_input['Cardboard']*carbon_saved_dict['Cardboard'] + dummy_input['Glass']*carbon_saved_dict['Glass'] + dummy_input['Metal']*carbon_saved_dict['Metal'] + dummy_input['Paper']*carbon_saved_dict['Paper'] + dummy_input['Plastic']*carbon_saved_dict['Plastic']
    # Append that new prediction to the past data
    past_data = past_data.append(dummy_input).reset_index(drop=True)
    os.remove(app.config['PAST_DATA'])
    past_data.to_csv(app.config['PAST_DATA'])

    objects = ['Cardboard', 'Glass', 'Metal', 'Paper', 'Plastic']
    # to date times
    past_data['Date'] = pd.to_datetime(past_data['Date'])
    number = past_data.groupby(pd.Grouper(key='Date', freq = 'Y')).sum().iloc[-1,:-1]
    carbon_temp = [number[i]*carbon_saved_dict[i] for i in objects]

    # Create subplots: use 'domain' type for Pie subplot
    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig.add_trace(go.Pie(labels=objects, values=number, name="Number"),
              1, 1)
    fig.add_trace(go.Pie(labels=objects, values=carbon_temp, name="Carbon footprint reduced"),
              1, 2)

    # Use `hole` to create a donut-like pie chart
    fig.update_traces(hole=.4, hoverinfo="label+percent+name", marker=dict(colors=colors), textinfo = 'value+label')
    fig.update_layout(
    title_text="Your recycling & carbon footprint saving record (Year To Date)",
    # Add annotations in the center of the donut pies.
    annotations=[dict(text='#items', x=0.18, y=0.5, font_size=20, showarrow=False),
                 dict(text='{} kg'.format(int(sum(carbon_temp))), x=0.82, y=0.5, font_size=20, showarrow=False)])
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    return graphJSON, float(dummy_input['carbon_footprint_reduce(kg)'])
