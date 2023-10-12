import uuid
import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__, suppress_callback_exceptions=True)

app.layout = html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '点我',
                    id='button-demo',
                    type='primary'
                ),
                html.Div(
                    id='button-demo-output'
                )
            ],
            direction='vertical'
        )
    ],
    style={
        'padding': 50
    }
)


def demo_render():

    new_uuid = str(uuid.uuid4())

    @app.callback(
        Output(f'demo-input-output-{new_uuid}', 'children'),
        Input(f'demo-input-{new_uuid}', 'value')
    )
    def dynamic_demo_callback(value):

        return f'已输入内容：{value}'

    return fac.AntdSpace(
        [
            fac.AntdInput(
                id=f'demo-input-{new_uuid}',
                placeholder='请输入'
            ),
            fac.AntdText(
                id=f'demo-input-output-{new_uuid}'
            )
        ]
    )


@app.callback(
    Output('button-demo-output', 'children'),
    Input('button-demo', 'nClicks'),
    prevent_initial_call=True,
    _allow_dynamic_callbacks=True
)
def demo_callback(nClicks):

    return demo_render()


if __name__ == '__main__':
    app.run(debug=True)
