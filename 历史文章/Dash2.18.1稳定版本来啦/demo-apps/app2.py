import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input, Output
from feffery_dash_utils.style_utils import style

# 这里on_error简单写个匿名函数示意
app = dash.Dash(__name__, on_error=lambda e: print(e))

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
    output=dict(
        demo_output1=Output("demo-output1", "children"),
        demo_output2=Output("demo-output2", "children"),
        demo_output3=Output("demo-output3", "children"),
    ),
    inputs=dict(nClicks=Input("demo-button", "nClicks")),
    prevent_initial_call=True,
)
def demo_callback(nClicks):
    # 仅在nClicks为奇数时触发
    if nClicks % 2 == 1:
        return dict(
            demo_output1=f"nClicks: {nClicks}",
            demo_output2=f"nClicks x 2: {nClicks*2}",
            demo_output3=f"nClicks x 3: {nClicks*3}",
        )

    # 故意触发错误
    raise Exception("自定义错误")


if __name__ == "__main__":
    app.run(debug=True)
