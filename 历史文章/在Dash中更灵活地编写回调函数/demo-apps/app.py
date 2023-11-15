import dash
from collections import defaultdict
import feffery_antd_components as fac
from dash.dependencies import Input, Output, State

app = dash.Dash(__name__)

app.layout = fac.AntdSpace(
    [
        fac.AntdSpace(
            [
                fac.AntdButton(
                    '按钮1',
                    type='primary',
                    id='demo-button1'
                ),
                fac.AntdButton(
                    '按钮2',
                    type='primary',
                    id='demo-button2'
                ),
                fac.AntdInput(
                    id='demo-input1',
                    placeholder='输入框1',
                    style={
                        'width': 150
                    }
                ),
                fac.AntdInput(
                    id='demo-input2',
                    placeholder='输入框2',
                    style={
                        'width': 150
                    }
                )
            ]
        ),
        fac.AntdSpace(
            [
                fac.AntdText(id='demo-output1'),
                fac.AntdText(id='demo-output2')
            ]
        )
    ],
    direction='vertical',
    style={
        'padding': 50
    }
)


@app.callback(
    [Output('demo-output1', 'children'),
     Output('demo-output2', 'children')],
    [Input('demo-button1', 'nClicks'),
     Input('demo-button2', 'nClicks')],
    [State('demo-input1', 'value'),
     State('demo-input2', 'value')],
    prevent_initial_call=True
)
def demo_callback(nClicks1, nClicks2, value1, value2):
    '''常规写法'''

    return [
        f'nClicks1: {nClicks1}, nClicks2: {nClicks2}',
        f'value1: {value1}, value2: {value2}'
    ]


# @app.callback(
#     [Output('demo-output1', 'children'),
#      Output('demo-output2', 'children')],
#     inputs=dict(
#         nClicks1=Input('demo-button1', 'nClicks'),
#         nClicks2=Input('demo-button2', 'nClicks')
#     ),
#     state=dict(
#         value1=State('demo-input1', 'value'),
#         value2=State('demo-input2', 'value')
#     ),
#     prevent_initial_call=True
# )
# def demo_callback(nClicks1, nClicks2, value1, value2):
#     '''字典化角色编排：仅Input、State字典化'''

#     return [
#         f'nClicks1: {nClicks1}, nClicks2: {nClicks2}',
#         f'value1: {value1}, value2: {value2}'
#     ]


# @app.callback(
#     output=dict(
#         content1=Output('demo-output1', 'children'),
#         content2=Output('demo-output2', 'children')
#     ),
#     inputs=dict(
#         nClicks1=Input('demo-button1', 'nClicks'),
#         nClicks2=Input('demo-button2', 'nClicks')
#     ),
#     state=dict(
#         value1=State('demo-input1', 'value'),
#         value2=State('demo-input2', 'value')
#     ),
#     prevent_initial_call=True
# )
# def demo_callback(nClicks1, nClicks2, value1, value2):
#     '''字典化角色编排：全部角色字典化'''

#     return dict(
#         content1=f'nClicks1: {nClicks1}, nClicks2: {nClicks2}',
#         content2=f'value1: {value1}, value2: {value2}'
#     )


# @app.callback(
#     output=dict(
#         content1=Output('demo-output1', 'children'),
#         content2=Output('demo-output2', 'children')
#     ),
#     inputs=dict(
#         nClicks1=Input('demo-button1', 'nClicks'),
#         nClicks2=Input('demo-button2', 'nClicks')
#     ),
#     state=dict(
#         input_values=dict(
#             value1=State('demo-input1', 'value'),
#             value2=State('demo-input2', 'value')
#         )
#     ),
#     prevent_initial_call=True
# )
# def demo_callback(nClicks1, nClicks2, input_values):
#     '''嵌套式字典化角色编排'''

#     return dict(
#         content1=f'nClicks1: {nClicks1}, nClicks2: {nClicks2}',
#         content2='value1: {value1}, value2: {value2}'.format(**input_values)
#     )


# @app.callback(
#     output=dict(
#         content1=Output('demo-output1', 'children'),
#         content2=Output('demo-output2', 'children')
#     ),
#     inputs=dict(
#         nClicks1=Input('demo-button1', 'nClicks'),
#         nClicks2=Input('demo-button2', 'nClicks')
#     ),
#     state=dict(
#         value1=State('demo-input1', 'value'),
#         value2=State('demo-input2', 'value')
#     ),
#     prevent_initial_call=True
# )
# def demo_callback(nClicks1, nClicks2, value1, value2):
#     '''字典化Output配合defaultdict'''

#     # 假设我们需要除了content1之外的其他角色默认输出为dash.no_update
#     output = defaultdict(
#         lambda: dash.no_update,
#         dict(
#             content1=f'nClicks1: {nClicks1}, nClicks2: {nClicks2}'
#         )
#     )

#     return {
#         key: output[key]
#         # 通过上下文遍历所有Output字典键名
#         for key in dash.ctx.outputs_grouping.keys()
#     }


if __name__ == '__main__':
    app.run(debug=True)
