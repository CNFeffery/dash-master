import dash
from dash import html
import feffery_antd_components as fac
import feffery_utils_components as fuc

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        # 粘性页首
        fac.AntdAffix(
            fuc.FefferyDiv(
                [
                    # 利用fac中的网格系统进行页首元素的排布
                    fac.AntdRow(
                        [
                            # logo+标题
                            fac.AntdCol(
                                fac.AntdSpace(
                                    [
                                        fac.AntdImage(
                                            src=dash.get_asset_url(
                                                './imgs/logo.png'
                                            ),
                                            height=54,
                                            preview=False
                                        ),
                                        fac.AntdText(
                                            'XX数据平台',
                                            strong=True,
                                            style={
                                                'fontSize': 32
                                            }
                                        )
                                    ]
                                ),
                                flex='none',
                                style={
                                    'height': 'auto'
                                }
                            ),

                            # 菜单栏
                            fac.AntdCol(
                                fac.AntdMenu(
                                    menuItems=[
                                        {
                                            'component': 'Item',
                                            'props': {
                                                'key': f'模块{i}',
                                                'title': f'模块{i}',
                                            }
                                        }
                                        for i in range(1, 6)
                                    ],
                                    defaultSelectedKey='模块1',
                                    mode='horizontal',
                                    style={
                                        'maxWidth': 600,
                                        'borderBottom': 'none'
                                    }
                                ),
                                flex='none',
                                style={
                                    'height': 'auto'
                                }
                            )
                        ],
                        align='middle',
                        justify='space-between',
                        wrap=False,  # 阻止自动换行
                        style={
                            'height': '100%'
                        }
                    )
                ],
                style={
                    'height': 64,
                    'padding': '0 25px',
                    'background': 'white',
                    'borderBottom': '1px solid #f0f0f0'
                }
            ),
            offsetTop=0
        ),

        # 固定侧边菜单+内容区
        fac.AntdRow(
            [
                # 固定侧边菜单
                fac.AntdCol(
                    fac.AntdAffix(
                        fuc.FefferyDiv(
                            fac.AntdMenu(
                                menuItems=[
                                    {
                                        'component': 'Item',
                                        'props': {
                                            'key': f'功能页面{i}',
                                            'title': f'功能页面{i}',
                                        }
                                    }
                                    for i in range(1, 25)
                                ],
                                defaultSelectedKey='功能页面1',
                                style={
                                    'height': '100%',
                                    'borderRight': 'none'
                                }
                            ),
                            scrollbar='simple',
                            style={
                                'width': 300,
                                'height': 'calc(100vh - 64px)',
                                'overflowY': 'auto'
                            }
                        ),
                        offsetTop=64  # 扣除页首所占高度
                    ),
                    flex='none'
                ),

                # 内容区
                fac.AntdCol(
                    [
                        html.Div(
                            fuc.FefferyDiv(
                                '示例内容'*2000,
                                shadow='always-shadow-light',
                                style={
                                    'borderRadius': 8,
                                    'background': 'white',
                                    'padding': 24
                                }
                            ),
                            style={
                                'minHeight': 'calc(100vh - 64px)',
                                'background': '#f0f2f5',
                                'padding': 50
                            }
                        )
                    ],
                    flex='auto'
                )
            ],
            wrap=False  # 阻止自动换行
        )
    ]
)

if __name__ == '__main__':
    app.run(debug=True)
