function addInput(elem) {
    let id = $(elem).parent().attr('id');
    $('#' + id).prev().val($(elem).text());
    $('#' + id).prev().attr('code_station', $(elem).attr('code_station'));
    $('#' + id).empty();
}

$("input[id^='input_']").bind("keypress keyup", function () {
    let value = $(this).val();
    let id = $(this).attr('id');
    $('#city_' + id).empty();
    if (value.length > 2) {
        ajax_search(value, id);
    }
});


$('#datepicker').datepicker({
    uiLibrary: 'bootstrap4'
});


