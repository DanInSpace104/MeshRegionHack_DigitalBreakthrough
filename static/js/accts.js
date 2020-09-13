// function saveOrg() {

// }

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
            data.map((el) => {
                $('#accts_list').append(`
                <li>
                <div class="row">
                    <div class="col-sm-7">
                        <h4 class="font-weight-bold text-info">Депозит, Сбербанк, 50 000 000</h4>
                        <span class="font-weight-bold">БИК:</span>
                        <span>46721476</span>,
                        <span class="font-weight-bold">Дата заключения:</span>
                        <span>03.05.2020</span><br>
                        <span class="font-weight-bold">Период</span>
                        <span>05.06.2020 - 10.20.2025</span>,
                        <span class="font-weight-bold">Процентная ставка:</span>
                        <span> 5,6%</span><br>
                    </div>
                    <div class="col-sm-3">
                    </div>
                </div>
                <br>
                <div class="row">
                    <div class="col-sm-5">
                        <div class="form-group row">
                            <label for="id1" class="col-form-label col-sm-3 text-right">Валюта:</label>
                            <div class="col-sm-9">
                                <select class="form-control" name="" id="id1">
                                    <option value="">RUR</option>
                                    <option value="">EUR</option>
                                    <option value="">USD</option>
                                </select>
                            </div>
                        </div>
                    </div>
                    <div class="col-sm-5">
                        <div class="form-group row">
                            <label for="id2" class="col-form-label col-sm-3 text-right">Остаток:</label>
                            <div class="col-sm-9">
                                <input class="form-control" type="text" id="id2">
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