let orgs;
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
            orgs = data
            console.log(orgs)
            data.map((d) => {
                $('#orgMain').append(`
                <option value="${d.id}/${d.name}">${d.name}</option>
                `)
            })
        }
    )
}

function saveOrg() {
    let org = $('#orgMain').val()
    let arr = org.split('/')
    let org_id = arr[0]
    let org_name = arr[1]
    document.cookie = `org_name=${org_name}`
    document.cookie = `org_id=${org_id}`
        // console.log(document.cookie)
}