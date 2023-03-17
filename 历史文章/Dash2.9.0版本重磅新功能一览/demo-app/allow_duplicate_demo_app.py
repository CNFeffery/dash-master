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
                    id='button-demo1'
                ),
                fac.AntdButton(
                    '按钮2',
                    id='button-demo2'
                )
            ]
        ),
        fac.AntdParagraph(
            id='output-demo'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('output-demo', 'children'),
    Input('button-demo1', 'nClicks'),
    prevent_initial_call=True
)
def trigger1(nClicks):

    return f'按钮1: {nClicks}'


@app.callback(
    Output('output-demo', 'children', allow_duplicate=True),
    Input('button-demo2', 'nClicks'),
    prevent_initial_call=True
)
def trigger2(nClicks):

    return f'按钮2: {nClicks}'

if __name__ == '__main__':
    app.run(debug=True)
