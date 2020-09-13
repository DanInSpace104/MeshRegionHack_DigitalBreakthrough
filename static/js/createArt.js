let banks;
getBanks();

function getBanks() {
    $.get(
        "/reports/bankbiks/", {},
        onBankBiksSuccess
    );
}

function onBankBiksSuccess(data) {
    banks = data
    data.map(d => {
        $('#banksSelect').append(`<option value="${d.id}">${d.name}</option>`);
        // $('#')
    })

    // {
    // data.foreach(d => $('#banksSelect').append(`<option value="${d.id}">${d.name}</option>'))
    // $('#banksSelect').append('<option value=""></option>');
    // banks = data;
}

function onBankChange() {
    console.log(banks[$('#banksSelect').val()]['bik']);
    // document.getElementById()
    $('#bikInput').val(banks[$('#banksSelect').val()]['bik']);
    // $('#bikInput').attr('disabled');
}