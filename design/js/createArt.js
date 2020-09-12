function send() {
    console.log(123);
    $.post(
        "http://localhost:8000/reports/banks/", {
            param1: "param1",
            param2: 2
        },
        onAjaxSuccess
    );

}

function onAjaxSuccess(data) {
    alert(data);
}