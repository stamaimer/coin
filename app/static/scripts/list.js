/**
 * Created by stamaimer on 16/8/19.
 */
$(document).ready(function(){
    $('.delete-exam').click(deleteStudent);
})
function deleteStudent() {
    var $this = $(this);
    var id = $(this).parents('tr').find('.id').text();
    $.ajax({
        url: '/exam',
        data: {id: id-0},
        type: 'DELETE',
        success: function (result) {
            $this.parents('tr').remove();
        }
    });
}