import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output
from feffery_dash_utils.style_utils import style

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdSpace(
            [
                f"Dash版本： {dash.__version__}",
                fac.AntdButton("点我试试", id="demo-button", type="primary"),
                fac.AntdText(id="demo-output1"),
                fac.AntdText(id="demo-output2"),
                fac.AntdText(id="demo-output3"),
            ],
            direction="vertical",
            align="center",
        )
    ],
    style=style(padding=50),
)


@app.callback(
    [Output(f"demo-output{i}", "children") for i in range(1, 4)],
    Input("demo-button", "nClicks"),
    prevent_initial_call=True,
)
def demo_callback(nClicks):
    # 仅在nClicks为奇数时触发
    if nClicks % 2 == 1:
        return (
            f"nClicks: {nClicks}",
            f"nClicks x 2: {nClicks*2}",
            f"nClicks x 3: {nClicks*3}",
        )

    # 不更新任何内容
    return dash.no_update


if __name__ == "__main__":
    app.run(debug=True)
