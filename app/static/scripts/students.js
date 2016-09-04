/**
 * Created by stamaimer on 16/8/19.
 */
$(document).ready(function () {
    $("#plus").click(function () {
        addRow();
        $("#plus").hide();
    });
    $(".delete").click(deleteStudent);
});
function addRow() {
    var tmp = "<tr class=\"score\">" +
        "<td contenteditable='true' id='new-student-id'></td>" +
        "<td contenteditable='true' id='new-student-name'></td>" +
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
    var $this = $(this);
    console.log('commit' + $(this));
    if (!$('#new-student-id').text() || !$('#new-student-name').text()) return;
    $.post("/student", {
        student_id: $('#new-student-id').text(),
        name: $('#new-student-name').text()
    }, function (result) {
        console.log(result);
        var tmp = "<tr class=\"score\">" +
            "<th scope=\"row\" class=\"student-id\">" + result.student_id + "</th>" +
            "<td style=\"display: none\" class=\"id\">" + result.id + "</td>" +
            "<td class=\"name\">" + result.name + "</td>" +
            "<td class=\"list-buttons-column\">" +
            "<a class=\"icon delete\" href=\"#\" title=\"删除\">" +
            "<span class=\"glyphicon glyphicon-trash\"></span>删除" +
            "</a>" +
            "</td>" +
            "</tr>";
        $this.parents('tr').remove();
        $("#plus").show();
        var $tmp = $(tmp);
        $tmp.parents('tr').find('.delete').click(deleteStudent);
        $('tbody').append(tmp)
    });
}
function cancel() {
    $(this).parents('tr').remove()
    console.log('cancel');
    $("#plus").show();
}
function deleteStudent() {
    var $this = $(this);
    var id = $(this).parents('tr').find('.id').text();
    $.ajax({
        url: '/student',
        data: {id: id-0},
        type: 'DELETE',
        success: function (result) {
            $this.parents('tr').remove();
        }
    });
}