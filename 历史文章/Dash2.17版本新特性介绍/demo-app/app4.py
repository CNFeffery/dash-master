import dash
import time
from dash import html


def demo_api():
    return {"now": time.time()}


# 在Dash对象实例化前添加自定义接口
dash.Dash.add_startup_route("demo-api", demo_api, ["GET"])

app = dash.Dash(__name__)

app.layout = html.Div("测试")

if __name__ == "__main__":
    app.run(debug=True)
