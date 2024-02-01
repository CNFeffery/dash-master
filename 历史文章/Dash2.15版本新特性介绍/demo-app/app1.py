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


@app.callback(
    Output('demo-output', 'children'),
    [Input('button1', 'nClicks'),
     Input('button2', 'nClicks')],
    prevent_initial_call=True
)
def handle_button_click(nClicks1, nClicks2):

    return '本次回调触发来源：{}'.format(
        dash.ctx.triggered_id
    )


if __name__ == '__main__':
    app.run(debug=True)
