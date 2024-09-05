window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        controlInputDisabled: (checkedList) => {

            // 计算当前已勾选项数量
            let count = 0;
            checkedList.forEach(checked => {
                if (checked) {
                    count++;
                }
            });
            if (count > 3) {
                // 强制将最近一次的勾选取消
                window.dash_clientside.set_props(
                    window.dash_clientside.callback_context.triggered_id,
                    {
                        checked: false
                    }
                )
                // 终止本次回调
                return window.dash_clientside.no_update;
            }
            // 借助outputs_list，针对性的更新本次回调触发项命中的输入框状态
            window.dash_clientside.callback_context.outputs_list.forEach(output => {
                if (output.id.index === window.dash_clientside.callback_context.triggered_id.index) {
                    // 切换命中目标输入框的禁用状态
                    window.dash_clientside.set_props(
                        output.id,
                        {
                            disabled: window.dash_clientside.callback_context.triggered[0].value
                        }
                    )
                }
            })

            return window.dash_clientside.no_update;
        }
    }
});