import dash
from dash import html
import feffery_antd_components as fac
from dash.dependencies import Input

app = dash.Dash(__name__)

app.layout = html.Div(
    [fac.AntdButton("示例按钮", id="demo-button", type="primary")],
    style={"padding": 50},
)


@app.callback(Input("demo-button", "nClicks"))
def no_output_callback(nClicks):
    print(f"nClicks: {nClicks}")


if __name__ == "__main__":
    app.run(debug=True)
