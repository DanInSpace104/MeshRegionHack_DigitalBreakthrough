function send() {
    console.log(123);
    $.get(
        "/reports/banks/", {},
        onAjaxSuccess
    );

}

function onAjaxSuccess(data) {
    console.log(data);

}