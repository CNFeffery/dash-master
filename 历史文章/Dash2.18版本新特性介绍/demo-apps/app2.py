import dash
from dash import html, set_props
import feffery_antd_components as fac
from dash.dependencies import Input, Output
from feffery_dash_utils.style_utils import style


def handle_global_error(e):
    # 利用服务端set_props()将错误信息集中抛出
    set_props(
        "error-message",
        {
            "children": fac.AntdMessage(
                content="触发id {}，错误信息 {}".format(dash.ctx.triggered_id, e),
                type="error",
            )
        },
    )


app = dash.Dash(__name__, on_error=handle_global_error)

app.layout = html.Div(
    [
        # 错误消息统一更新目标
        fac.Fragment(id="error-message"),
        fac.AntdSpace(
            [
                fac.AntdSpace(
                    [
                        fac.AntdButton("全局错误示例1", id="trigger-global-error1"),
                        fac.AntdText(id="trigger-global-error-output1"),
                    ]
                ),
                fac.AntdSpace(
                    [
                        fac.AntdButton("全局错误示例2", id="trigger-global-error2"),
                        fac.AntdText(id="trigger-global-error-output2"),
                    ]
                ),
            ],
            direction="vertical",
            style=style(width="100%"),
        ),
    ],
    style=style(padding=100),
)


@app.callback(
    Output("trigger-global-error-output1", "children"),
    Input("trigger-global-error1", "nClicks"),
    prevent_initial_call=True,
)
def global_error_demo1(nClicks):
    """示例回调函数1"""
    if nClicks % 2 == 0:
        # 触发示例错误
        1 / 0

    return f"nClicks: {nClicks}"


def handle_local_error(e):
    # 利用服务端set_props()将错误信息集中抛出
    set_props(
        "error-message",
        {
            "children": fac.AntdMessage(
                content="🧐异常发生，异常信息 {}".format(e),
                type="error",
            )
        },
    )


@app.callback(
    Output("trigger-global-error-output2", "children"),
    Input("trigger-global-error2", "nClicks"),
    on_error=handle_local_error,
    prevent_initial_call=True,
)
def global_error_demo2(nClicks):
    """示例回调函数2"""
    if nClicks % 2 == 0:
        # 触发示例错误
        raise Exception("这是一个自定义错误")

    return f"nClicks: {nClicks}"


if __name__ == "__main__":
    app.run(debug=True)
