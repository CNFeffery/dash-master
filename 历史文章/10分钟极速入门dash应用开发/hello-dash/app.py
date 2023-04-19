# 相关包的导入
import dash  # dash应用核心
import pandas as pd
from dash import html  # dash自带的原生html组件库
import feffery_antd_components as fac  # fac通用组件库
from dash.dependencies import Input, Output, State  # 用于构建应用交互功能的不同角色


# 实例化Dash()对象
app = dash.Dash(__name__)

# 创建示例表格
demo_df = pd.DataFrame(
    {
        '字段1': [f'类别{i}' for i in range(1, 11)],
        '字段2': [10*i for i in range(10)],
        '字段3': [(pd.Timestamp('2023-01-01') + pd.Timedelta(days=i)).strftime('%Y-%m-%d')
                for i in range(10)]
    }
)

# 为dash应用定义初始元素
app.layout = html.Div(
    [
        # 这里以fac中的警告提示组件为例
        # 文档地址：https://fac.feffery.tech/AntdAlert
        fac.AntdAlert(
            message='Hello Dash!',
            description=f'当前应用dash版本：{dash.__version__} fac版本：{fac.__version__}',
            showIcon=True
        ),
        # 放置水平分割虚线
        fac.AntdDivider(isDashed=True),
        fac.AntdForm(
            [
                fac.AntdFormItem(
                    fac.AntdSelect(
                        id='field1-range',
                        options=[
                            {
                                'label': x,
                                'value': x
                            }
                            for x in demo_df['字段1'].unique()
                        ],
                        mode='multiple',
                        maxTagCount='responsive',
                        style={
                            'width': 200
                        }
                    ),
                    label='字段1'
                ),
                fac.AntdFormItem(
                    fac.AntdSlider(
                        id='field2-range',
                        min=0,
                        max=100,
                        range=True,
                        defaultValue=[0, 100],
                        style={
                            'width': 150
                        }
                    ),
                    label='字段2'
                ),
                fac.AntdFormItem(
                    fac.AntdDateRangePicker(
                        id='field3-range',
                        defaultPickerValue=demo_df['字段3'].min(),
                        style={
                            'width': 200
                        }
                    ),
                    label='字段3'
                ),
                fac.AntdButton(
                    '查询',
                    id='execute-query',
                    icon=fac.AntdIcon(
                        icon='antd-search'
                    ),
                    type='primary'
                )
            ],
            layout='inline',
            style={
                'marginBottom': 15
            }
        ),
        html.Div(id='table-result-container')
    ],
    style={
        # 这里基于css中的padding参数，设置上下内边距50像素，左右内边距100像素
        'padding': '50px 100px'
    }
)


@app.callback(
    Output('table-result-container', 'children'),
    Input('execute-query', 'nClicks'),
    [State('field1-range', 'value'),
     State('field2-range', 'value'),
     State('field3-range', 'value')]
)
def query_table(nClicks, field1_range, field2_range, field3_range):

    demo_df_copy = demo_df.copy()

    if field1_range:
        demo_df_copy.query('字段1 == @field1_range', inplace=True)

    if field2_range:
        demo_df_copy.query(f'{field2_range[0]} <= 字段2 <= {field2_range[1]}',
                           inplace=True)

    if field3_range:
        demo_df_copy.query(f'"{field3_range[0]}" <= 字段3 <= "{field3_range[1]}"',
                           inplace=True)

    if not demo_df_copy.empty:
        return fac.AntdTable(
            columns=[
                {
                    'title': column,
                    'dataIndex': column
                }
                for column in demo_df_copy.columns
            ],
            data=demo_df_copy.to_dict('records'),
            bordered=True
        )

    # 否则返回无匹配数据提示
    return fac.AntdEmpty(
        description='当前条件组合下无匹配数据'
    )


if __name__ == '__main__':
    app.run(debug=True)
