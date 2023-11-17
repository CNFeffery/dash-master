import dash
from dash import html, dcc
import feffery_antd_components as fac
from dash.dependencies import Input, Output, ClientsideFunction

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Interval(
            id='interval',
            interval=1000  # 每秒触发一次
        ),
        fac.AntdStatistic(
            id='current-datetime',
            title='当前时间'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)

app.clientside_callback(
    ClientsideFunction(
        namespace='clientside',
        function_name='update_datetime'
    ),
    Output('current-datetime', 'value'),
    Input('interval', 'n_intervals')
)

if __name__ == '__main__':
    app.run(debug=True)
