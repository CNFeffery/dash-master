import dash
from dash import html, set_props
import feffery_antd_components as fac
from dash.dependencies import Input

app = dash.Dash(__name__)

app.layout = html.Div(
    [
        fac.AntdButton("翻转颜色", id="reverse-color", type="primary"),
        fac.AntdRow(
            [
                fac.AntdCol(id="left-block", span=12, style={"background": "white"}),
                fac.AntdCol(id="right-block", span=12, style={"background": "black"}),
            ],
            style={"height": 500},
        ),
    ],
    style={"padding": 50},
)


@app.callback(Input("reverse-color", "nClicks"))
def reverse_color(nClicks):
    if nClicks % 2 == 0:
        set_props("left-block", {"style": {"background": "white"}})
        set_props("right-block", {"style": {"background": "black"}})

    else:
        set_props("left-block", {"style": {"background": "black"}})
        set_props("right-block", {"style": {"background": "white"}})


if __name__ == "__main__":
    app.run(debug=True)
