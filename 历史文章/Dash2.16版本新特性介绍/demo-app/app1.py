import time
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdSwitch(
            id='switch-demo',
            checked=False
        ),
        html.Div(id='message-container')
    ],
    style={
        'padding': 50
    }
)


@app.callback(
    Output('message-container', 'children'),
    Input('switch-demo', 'checked'),
    running=[
        [Output('switch-demo', 'loading'), True, False]
    ],
    prevent_initial_call=True
)
def switch_demo(checked):

    time.sleep(1)

    return fac.AntdMessage(
        content='已开启' if checked else '已关闭',
        type='success'
    )


if __name__ == '__main__':
    app.run(debug=False)

