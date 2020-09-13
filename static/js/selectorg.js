function saveOrg() {

}

function getOrg() {
    $.get(
        "/reports/companys/", {},
        onComapanysSuccess
    )
}

function onComapanysSuccess(data) {
    // for (data) {

    // }
}