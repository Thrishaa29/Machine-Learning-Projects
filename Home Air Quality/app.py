# app.py
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import plotly.graph_objs as go
from dash_extensions import EventListener

# Load data
df = pd.read_csv('anomaly_detection_alerts.csv', parse_dates=['timestamp'])
df.set_index('timestamp', inplace=True)

# Initialize app
app = dash.Dash(__name__)
app.title = "Elderly Monitoring Dashboard"
server = app.server  # for deployment

# Audio component
audio = html.Audio(id="audio-player", src="/assets/alert.mp3", controls=False, autoPlay=False)

app.layout = html.Div([
    html.H1("🏠 Elderly Home Air Quality Dashboard", style={'textAlign': 'center'}),
    
    dcc.DatePickerRange(
        id='date-range',
        start_date=df.index.min().date(),
        end_date=df.index.max().date()
    ),
    
    dcc.Graph(id='co-graph'),
    
    html.H3("⚠️ Critical Alerts"),
    dcc.Graph(id='alert-table'),

    audio,  # Add audio component
    html.Div(id='sound-trigger')  # Used to activate audio
])

@app.callback(
    [Output('co-graph', 'figure'),
     Output('alert-table', 'figure'),
     Output('sound-trigger', 'children')],
    [Input('date-range', 'start_date'),
     Input('date-range', 'end_date')]
)
def update_graph(start_date, end_date):
    filtered = df.loc[start_date:end_date]

    # CO Graph
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=filtered.index, y=filtered['COValue'], mode='lines', name='COValue'))
    fig.add_trace(go.Scatter(x=filtered.index, y=[9]*len(filtered), mode='lines', name='Warning (9ppm)', line=dict(dash='dash', color='orange')))
    fig.add_trace(go.Scatter(x=filtered.index, y=[35]*len(filtered), mode='lines', name='Danger (35ppm)', line=dict(dash='dash', color='red')))

    anomaly_points = filtered[filtered['anomaly'] == 1]
    fig.add_trace(go.Scatter(x=anomaly_points.index, y=anomaly_points['COValue'],
                             mode='markers', name='Anomaly', marker=dict(color='black', size=6)))
    fig.update_layout(title="CO Sensor Data with Anomalies", xaxis_title="Time", yaxis_title="CO (ppm)")

    # Alerts Table
    critical = filtered[filtered['critical_alert']]
    alert_fig = go.Figure(data=[go.Table(
        header=dict(values=list(critical.reset_index().columns),
                    fill_color='lightgray', align='left'),
        cells=dict(values=[critical.reset_index()[col] for col in critical.reset_index().columns],
                   fill_color='white', align='left'))
    ])
    alert_fig.update_layout(height=300)

    # 🔊 Trigger sound only if critical alert exists in window
    sound_trigger = html.Script("document.getElementById('audio-player').play();") if not critical.empty else ""

    return fig, alert_fig, sound_trigger

# Run the app
if __name__ == '__main__':
    app.run(debug=True)


