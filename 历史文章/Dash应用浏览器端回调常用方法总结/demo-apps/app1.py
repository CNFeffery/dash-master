import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdButton(
            '打开模态框',
            id='open-modal',
            type='primary'
        ),
        fac.AntdModal(
            fac.AntdParagraph('测试内容'*100),
            id='modal',
            title='模态框示例'
        )
    ],
    style={
        'padding': '50px 100px'
    }
)

app.clientside_callback(
    '(nClicks) => true',
    Output('modal', 'visible'),
    Input('open-modal', 'nClicks'),
    prevent_initial_call=True
)

if __name__ == '__main__':
    app.run(debug=True)
