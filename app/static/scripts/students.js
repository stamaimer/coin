/**
 * Created by stamaimer on 16/8/19.
 */
$(document).ready(function () {
    $("#plus").click(function () {
        addRow();
        $("#plus").hide();
    });
});
function addRow() {
    var tmp = "<tr class=\"score\">" +
        "<td contenteditable='true'></td>" +
        "<td contenteditable='true'></td>" +
        "<td class=\"list-buttons-column\">" +
        "<a class=\"icon commit\" href=\"#\" title=\"确定\">" +
        "<span class=\"glyphicon glyphicon-ok\"></span>确定" +
        "</a>" +
        "<a class=\"icon cancel\" href=\"#\" title=\"取消\">" +
        "<span class=\"glyphicon glyphicon-remove\"></span>取消" +
        "</a>" +
        "</td>" +
        "</tr>";
    var $tmp = $(tmp)
    $tmp.find('.commit').click(commit);
    $tmp.find('.cancel').click(cancel);
    $('#students').append($tmp);
}
function commit() {
    console.log('commit'+$(this));
    $("#plus").show();
}
function cancel() {
    $(this).parents('tr').remove()
    console.log('cancel');
    $("#plus").show();
}