getOrg();

function getOrg() {

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));

        }
    });
    $.get(
        "/reports/companys/", {

            'X-CSRFToken': $.cookie('csrftoken'),
            'sessionid': $.cookie('sessionid'),
        },
        (data) => {
            data.map((d) => {
                $('#orgMain').append(`
                <option value="${d.id}">${d.name}</option>
                 `)
            })
        }
    )
}

function seveOrg() {

}