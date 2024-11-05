import dash
from dash import html
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
from dash.dependencies import Input, Output, ALL

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        f"Dash版本：{dash.__version__}",
        html.Div(
            fac.AntdSpace(
                [
                    fac.AntdSwitch(
                        id={"type": "test-switch", "index": i}, checked=False
                    )
                    for i in range(1000)
                ],
                wrap=True,
            ),
            style=style(
                height=300, overflow="auto", padding=5, border="1px solid #bfbfbf"
            ),
        ),
        fac.AntdText("已打开开关数量：0", id="test-output"),
    ],
    style=style(padding=50),
)

app.clientside_callback(
    "(checked_list) => `已打开开关数量：${checked_list.filter(Boolean).length}`",
    Output("test-output", "children"),
    Input({"type": "test-switch", "index": ALL}, "checked"),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run(debug=True)
