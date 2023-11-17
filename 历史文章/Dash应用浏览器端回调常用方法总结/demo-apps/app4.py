import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdButton(
            '新的消息',
            id='new-message',
            type='primary'
        ),
        html.Div(id='new-message-container')
    ],
    style={
        'padding': '50px 100px'
    }
)

app.clientside_callback(
    '''(nClicks) => ({
        props: {
            content: "新的消息，nClicks：" + nClicks,
            type: "info"
        },
        type: "AntdMessage",
        namespace: "feffery_antd_components"
        
    })''',
    Output('new-message-container', 'children'),
    Input('new-message', 'nClicks'),
    prevent_initial_call=True
)

if __name__ == '__main__':
    app.run(debug=True)
