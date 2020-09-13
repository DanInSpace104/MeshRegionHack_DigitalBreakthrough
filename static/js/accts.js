let acts;
getAccts();

function getAccts() {

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));

        }
    });
    $.get(
        "/reports/superaccounts/", {

        },
        (data) => {
            acts = data;
            data.map((el) => {
                $('#accts_list').append(`
                <li>
                <div class="row">
                    <div class="col-sm-9">
                        <h4 class="font-weight-bold text-info">${el.acc_type}, ${el.bank_name}, ${el.summ}</h4>
                        <span class="font-weight-bold">БИК:</span>
                        <span>${el.bik}</span>,
                        <span class="font-weight-bold">Дата заключения:</span>
                        <span>${el.contract_create_date}</span>,
                        <span class="font-weight-bold">Валюта</span>
                        <span>${el.currency_code}</span><br>
                        <span class="font-weight-bold">Период</span>
                        <span>${el.contract_begin_date} - ${el.contract_end_date}</span>,
                        <span class="font-weight-bold">Процентная ставка:</span>
                        <span>${el.settlement_rate}</span>
                        <br>
                    </div>
                    <div class="col-sm-3">
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-sm-5">
                        <div class="form-group row">
                            <label for="acct${el.id}" class="col-form-label col-sm-3 text-right">Остаток:</label>
                            <div class="col-sm-9">
                                <input class="form-control" type="number" step="0.01" value="${el.balance}" id="acct${el.id}">
                            </div>
                        </div>
                    </div>
                </div>
                <hr>
            </li>
                `)
            })
        }
    )
}

function onSave() {
    let res = {}
    acts.map(
        (el) => {
            res[el.id] = $(`#acct${el.id}`).val()
        }
    )
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));

        }
    });
    $.post(
        "/reports/change_accs/", {
            ...res
        },
    );
    // window.location.href = "/reports/accts/";
}

function onCreate() {
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        },
        dataType: "text"
    });
    // let res = [];

    $.post(
        "/reports/reports/", {
            data: JSON.stringify(acts)
        },
        downloadXLSX
    );
    // window.location.href = "/reports/accts/";
}

function downloadXLSX(data) {
    console.log(data);
    linkText = '/static/' + data;


    var link = document.createElement('a');



    let pdflink = linkText;



    link.setAttribute('href', pdflink);



    //pdfname - имя файла для загрузки (как он будет называться у посетителя)

    pdfname = 'report.xlsx';

    link.setAttribute('download', pdfname);



    link.setAttribute('target', '_blank');



    link.style.display = 'none';



    document.body.appendChild(link);



    link.click();



    document.body.removeChild(link);
    // var bytes = new Uint8Array(data); // pass your byte response to this constructor

    // var blob = new Blob([bytes], { type: "application/vnd.ms-excel" }); // change resultByte to bytes 
    // var link = document.createElement('a');
    // link.href = window.URL.createObjectURL(blob);
    // link.download = "myFileName.xls";
    // link.click();
}