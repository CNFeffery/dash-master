import uuid
import dash
from dash import html, dcc
import feffery_antd_components as fac
import feffery_utils_components as fuc
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        dcc.Store(
            id='demo-store',
            data={}
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '初始化dict字典',
                                    id='init-dict'
                                ),
                                fac.AntdDivider(
                                    isDashed=True
                                ),
                                fac.AntdSpace(
                                    [
                                        fac.AntdButton(
                                            'dict值加1',
                                            id='dict-plus1'
                                        ),
                                        fac.AntdButton(
                                            'dict值减1',
                                            id='dict-minus1'
                                        ),
                                        fac.AntdButton(
                                            'dict值乘10',
                                            id='dict-multiply10'
                                        ),
                                        fac.AntdButton(
                                            'dict值除10',
                                            id='dict-divide10'
                                        )
                                    ]
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        )
                    ],
                    span=12
                ),
                fac.AntdCol(
                    [
                        fac.AntdSpace(
                            [
                                fac.AntdButton(
                                    '初始化list列表',
                                    id='init-list'
                                ),
                                fac.AntdDivider(
                                    isDashed=True
                                ),
                                fac.AntdSpace(
                                    [
                                        fac.AntdButton(
                                            'append值',
                                            id='list-append'
                                        ),
                                        fac.AntdButton(
                                            'prepend值',
                                            id='list-prepend'
                                        ),
                                        fac.AntdButton(
                                            '翻转值',
                                            id='list-reverse'
                                        ),
                                        fac.AntdButton(
                                            '修改第2位值',
                                            id='list-alter-second'
                                        ),
                                        fac.AntdButton(
                                            '清空值',
                                            id='list-clear'
                                        )
                                    ]
                                )
                            ],
                            direction='vertical',
                            style={
                                'width': '100%'
                            }
                        )
                    ],
                    span=12
                )
            ],
            gutter=25
        ),
        fac.AntdDivider(
            isDashed=True
        ),
        fuc.FefferyJsonViewer(
            id='show-demo-store'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('show-demo-store', 'data'),
    Input('demo-store', 'data')
)
def show_demo_store(data):

    return data


@app.callback(
    Output('demo-store', 'data'),
    Input('init-dict', 'nClicks'),
    prevent_initial_call=True
)
def init_dict(nClicks):

    patch = dash.Patch()
    patch.dict = 1

    return patch


@app.callback(
    Output('demo-store', 'data', allow_duplicate=True),
    Input('init-list', 'nClicks'),
    prevent_initial_call=True
)
def init_list(nClicks):

    patch = dash.Patch()
    patch.list = []

    return patch


@app.callback(
    Output('demo-store', 'data', allow_duplicate=True),
    [Input('dict-plus1', 'nClicks'),
     Input('dict-minus1', 'nClicks'),
     Input('dict-multiply10', 'nClicks'),
     Input('dict-divide10', 'nClicks')],
    prevent_initial_call=True
)
def dict_value_operation(plus1,
                         minus1,
                         multiply10,
                         divide10):
    '''这个例子也顺便体现了，即使有了allow_duplicate=True机制，有些时候走ctx条件判断仍然更方便'''

    if dash.ctx.triggered_id == 'dict-plus1':
        patch = dash.Patch()
        patch.dict += 1

    elif dash.ctx.triggered_id == 'dict-minus1':
        patch = dash.Patch()
        patch.dict -= 1

    elif dash.ctx.triggered_id == 'dict-multiply10':
        patch = dash.Patch()
        patch.dict *= 10

    elif dash.ctx.triggered_id == 'dict-divide10':
        patch = dash.Patch()
        patch.dict /= 10

    return patch


@app.callback(
    Output('demo-store', 'data', allow_duplicate=True),
    [Input('list-append', 'nClicks'),
     Input('list-prepend', 'nClicks'),
     Input('list-reverse', 'nClicks'),
     Input('list-alter-second', 'nClicks'),
     Input('list-clear', 'nClicks'), ],
    prevent_initial_call=True
)
def list_value_operation(list_append,
                         list_prepend,
                         list_reverse,
                         list_alter_second,
                         list_clear):

    if dash.ctx.triggered_id == 'list-append':
        patch = dash.Patch()
        patch.list.append(str(uuid.uuid4()))

    elif dash.ctx.triggered_id == 'list-prepend':
        patch = dash.Patch()
        patch.list.prepend(str(uuid.uuid4()))

    elif dash.ctx.triggered_id == 'list-reverse':
        patch = dash.Patch()
        patch.list.reverse()

    elif dash.ctx.triggered_id == 'list-alter-second':
        patch = dash.Patch()
        patch.list[2] = 99999

    elif dash.ctx.triggered_id == 'list-clear':
        patch = dash.Patch()
        patch.list.clear()

    return patch


if __name__ == '__main__':
    app.run(debug=True)
