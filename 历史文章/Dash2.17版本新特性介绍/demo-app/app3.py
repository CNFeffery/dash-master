import dash
import time
import diskcache
import feffery_antd_components as fac
from dash.dependencies import Input
from dash import html, set_props, DiskcacheManager

cache = diskcache.Cache("./cache")
background_callback_manager = DiskcacheManager(cache)

app = dash.Dash(__name__, background_callback_manager=background_callback_manager)

app.layout = html.Div(
    [
        fac.AntdButton(
            "执行任务",
            id="execute-task",
            type="primary",
            autoSpin=True,
            loadingChildren="执行中",
        ),
        fac.AntdFormItem(
            fac.AntdProgress(id="task-progress", percent=0, style={"width": 300}),
            label="任务进度",
        ),
    ],
    style={"padding": 50},
)


@app.callback(Input("execute-task", "nClicks"), background=True, interval=500)
def execute_task(nClicks):
    for i in range(1, 6):
        set_props("task-progress", {"percent": i * 20})
        time.sleep(1)

    set_props("execute-task", {"loading": False})


if __name__ == "__main__":
    app.run(debug=True)
