let banks;
let currencys;
getBanks();
getCurrencys();
console.log($.cookie('csrftoken'))

function getBanks() {
    $.get(
        "/reports/bankbiks/", {},
        onBankBiksSuccess
    );
}

function getCurrencys() {
    $.get(
        "/reports/currencys/", {},
        (data) => {
            currencys = data;
            data.map(d => $('#currencySelect').append(`<option value="${d.id}">${d.name} ${d.code}</option>`));
        }
    );
}

function onBankBiksSuccess(data) {
    banks = data
    data.map(d => {
        $('#banksSelect').append(`<option value="${d.id}">${d.name}</option>`);
    })
}

function onBankChange() {
    $('#bikInput').val(banks[$('#banksSelect').val()]['bik']);
}

function onSubmit() {
    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));

        }
    });
    $.post(
        "/reports/accounts/", {
            'acc_type': $('#acc_typeSelect').val(),
            'money': $('#moneyInput').val(),
            'contract_begin_date': $('#begDateInput').val(),
            'currency': $('#currencySelect').val(),
            'contract_end_date': $('#endDateInput').val(),
            'settlement_rate': $('#settlementRateInput').val(),
            'bank': $('#banksSelect').val(),
            'company': 1,
            'X-CSRFToken': $.cookie('csrftoken'),
            'sessionid': $.cookie('sessionid'),
        },
    );
}