window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        update_datetime: (n_intervals) => {
            return `${new Date().toLocaleDateString().replaceAll("/", "-")} ${new Date().toLocaleTimeString()}`
        }
    }
});
