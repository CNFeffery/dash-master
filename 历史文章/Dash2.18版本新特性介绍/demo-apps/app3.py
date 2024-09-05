import dash
from dash import html
import feffery_antd_components as fac
from feffery_dash_utils.style_utils import style
from dash.dependencies import Input, Output, ALL, ClientsideFunction

app = dash.Dash(__name__, assets_folder="app3_assets")

app.layout = html.Div(
    [
        fac.AntdSpace(
            [
                fac.AntdText("至多禁用3个输入框"),
                *[
                    fac.AntdSpace(
                        [
                            fac.AntdTooltip(
                                fac.AntdSwitch(
                                    id={
                                        "type": "control-input-disabled",
                                        "index": f"item{i}",
                                    }
                                ),
                                title=f"禁用输入框{i}",
                            ),
                            fac.AntdInput(
                                id={"type": "input", "index": f"item{i}"},
                                placeholder=f"输入框{i}",
                                style=style(width=256),
                            ),
                        ]
                    )
                    for i in range(10)
                ],
            ],
            direction="vertical",
            style=style(width="100%"),
        )
    ],
    style=style(padding=50),
)


app.clientside_callback(
    ClientsideFunction(
        namespace="clientside",
        function_name="controlInputDisabled",
    ),
    Output({"type": "input", "index": ALL}, "disabled"),
    Input(
        {
            "type": "control-input-disabled",
            "index": ALL,
        },
        "checked",
    ),
    prevent_initial_call=True,
)

if __name__ == "__main__":
    app.run(debug=True)
