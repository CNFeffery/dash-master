import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '按钮1',
                    id='button1',
                    type='primary'
                ),
                fac.AntdButton(
                    '按钮2',
                    id='button2',
                    type='primary'
                )
            ]
        ),
        fac.AntdParagraph(id='demo-output')
    ],
    style={
        'padding': 50
    }
)


app.clientside_callback(
    '''(nClicks1, nClicks2) => {
        // 打印本次回调上下文信息
        console.log(dash_clientside.callback_context)
    }''',
    Output('demo-output', 'children'),
    [Input('button1', 'nClicks'),
     Input('button2', 'nClicks')],
    prevent_initial_call=True
)

if __name__ == '__main__':
    app.run(debug=True)
