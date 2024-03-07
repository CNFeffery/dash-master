import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdButton(
            '点我',
            id='trigger-demo',
            type='primary'
        ),
        fac.AntdRow(
            [
                fac.AntdCol(
                    fac.AntdCenter(
                        id=f'demo-block{i+1}'
                    ),
                    span=4,
                    style={
                        'padding': 5
                    }
                )
                for i in range(30)
            ]
        )
    ],
    style={
        'padding': 50
    }
)

app.clientside_callback(
    '''(nClicks) => {
        // 内部自由批量更新其他目标属性
        for ( let i = 1; i <= 30; i++ ) {
            // 调用set_props()
            window.dash_clientside.set_props(
                `demo-block${i}`,
                {
                    children: `nClicks: ${nClicks || 0}`,
                    style: {
                        height: 100,
                        background: '#262626',
                        color: 'white',
                        borderRadius: 4,
                        fontSize: Math.min(14 + nClicks, 24)
                    }
                }
            )
        }

        return window.dash_clientside.no_update;
    }''',
    Output('trigger-demo', 'id'),
    Input('trigger-demo', 'nClicks')
)

if __name__ == '__main__':
    app.run(debug=False)
