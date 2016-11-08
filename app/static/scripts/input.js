/**
 * Created by stamaimer on 16/8/19.
 */
jQuery.fn.selectText = function () {
    var doc = document;
    var element = this[0];
    console.log(this, element);
    if (doc.body.createTextRange) {
        var range = document.body.createTextRange();
        range.moveToElementText(element);
        range.select();
    } else if (window.getSelection) {
        var selection = window.getSelection();
        var range = document.createRange();
        range.selectNodeContents(element);
        selection.removeAllRanges();
        selection.addRange(range);
    }
};
(function ($) {
    $.fn.clickToggle = function (func1, func2) {
        var funcs = [func1, func2];
        this.data('toggleclicked', 0);
        this.click(function () {
            var data = $(this).data();
            var tc = data.toggleclicked;
            $.proxy(funcs[tc], this)();
            data.toggleclicked = (tc + 1) % 2;
        });
        return this;
    };
}(jQuery));
$(document).ready(function () {
    $('td').keypress(function (evt) {
        if (evt.which == 13) {
            event.preventDefault();
            var cellindex = $(this).index() - 1
            // get next row, then select same cell index
            var rowindex = $(this).parents('tr').index() + 1
            $(this).parents('tbody').find('tr:eq(' + rowindex + ') td:eq(' + cellindex + ')').focus()
        }
    });
    $('td').focus(function (evt) {
        $(this).selectText();
    });
    $('#submit').click(function () {
        if (!$("#exam-name").val()) {
            $("#exam-name").parent().addClass('has-error');
            return;
        }
        var arr = [];
        if (!$("#exam-id").val()) {
            $.ajax({
                url: '/exam',
                data: {name: $("#exam-name").val()},
                type: 'POST',
                success: function (result) {
                    sendData(result.id, result.name);
                }
            })
        } else {
            sendData($("#exam-id").val(), $("#exam-name").val());
        }
    });
    $('#calc').click(function () {
        autoCalc();
    });
    $('thead th').clickToggle(function (evt) {
        var tmp = $('.score').sort(sortBy($(this).index()+1));
        tmp.detach().prependTo('#score tbody');
    }, function (evt) {
        var tmp = $('.score').sort(sortRevertBy($(this).index()+1));
        tmp.detach().prependTo('#score tbody');
    });
})
;

function autoCalc() {
    $('.score').each(function (index, value) {
        var sum3 = parseInt($(this).find('.yw').text()) + parseInt($(this).find('.sx').text()) + parseInt($(this).find('.yy').text());
        $(this).find('.sum_3').text(sum3);
        sortBy3();
    });
    calcAverage()
}


function calcAverage() {
    for(var i = 1 ;i <= 20;i++){
        var sum = 0;
        var count = 0;
        $('.included').each(function (index, value) {
            var tmp = parseFloat($(this).find('td').eq(i+1).text());
            if( tmp!= 0){
                sum+=tmp;
                count++;
            }
        });
        $('.average').find('td').eq(i).text((sum/count || 0).toFixed(2));
    }
}


function sortBy3() {
    $('.score')
        .find('.sum_3')
        .sort(function (a, b) {
            return b.innerText - a.innerText
        })
        .next()
        .each(function (index) {
            $(this).text(index + 1)
        });
}

function sortBy5() {
    $('.score')
        .find('td:eq(14)')
        .sort(function (a, b) {
            return b.innerText - a.innerText
        })
        .next()
        .each(function (index) {
            $(this).text(index + 1)
        });
}
function sortBy(index) {
    return function (a, b) {
        //if (isNaN($(b).children().eq(index).text()) || isNaN($(a).children().eq(index).text()) || $(b).children().eq(index).text() == $(a).children().eq(index).text())
        //    return -1;
        return $(b).children().eq(index).text() - $(a).children().eq(index).text()
    }
}
function sortRevertBy(index) {
    return function (a, b) {
        //if (isNaN($(b).children().eq(index).text()) || isNaN($(a).children().eq(index).text()) || $(b).children().eq(index).text() == $(a).children().eq(index).text())
        //    return 1;
        return $(a).children().eq(index).text() - $(b).children().eq(index).text()
    }
}
function sendData(examId, examName) {
    var data = {};
    data.exam_id = examId;
    data.exam_name = examName;
    data.scores = [];
    $('.score').each(function (i) {
        var score = {};
        score.student_id = $(this).find('.student_id').text();
        score.yw = $(this).find('.yw').text();
        score.sx = $(this).find('.sx').text();
        score.yy = $(this).find('.yy').text();
        score.wl_hg = $(this).find('.wl_hg').text();
        score.wl_dj = $(this).find('.wl_dj').text();
        score.hx_hg = $(this).find('.hx_hg').text();
        score.hx_dj = $(this).find('.hx_dj').text();
        score.sw = $(this).find('.sw').text();
        score.ls = $(this).find('.ls').text();
        score.zz = $(this).find('.zz').text();
        score.dl = $(this).find('.dl').text();

        score.yw_stand = $(this).find('.yw_stand').text();
        score.sx_stand = $(this).find('.sx_stand').text();
        score.yy_stand = $(this).find('.yy_stand').text();
        score.wl_stand = $(this).find('.wl_stand').text();
        score.hx_stand = $(this).find('.hx_stand').text();
        score.sw_stand = $(this).find('.sw_stand').text();
        score.ls_stand = $(this).find('.ls_stand').text();
        score.zz_stand = $(this).find('.zz_stand').text();
        score.dl_stand = $(this).find('.dl_stand').text();
        score.sum_3 = $(this).find('.sum_3').text();
        score.class_rank_3 = $(this).find('.class_rank_3').text();
        score.grade_rank_3 = $(this).find('.grade_rank_3').text();
        data.scores.push(score);
    });
    data.yw_av = $('.yw_av').text();
    data.sx_av = $('.sx_av').text();
    data.yy_av = $('.yy_av').text();
    data.wl_hg_av = $('.wl_hg_av').text();
    data.hx_hg_av = $('.hx_hg_av').text();
    data.wl_dj_av = $('.wl_dj_av').text();
    data.hx_dj_av = $('.hx_dj_av').text();
    data.sw_av = $('.sw_av').text();
    data.ls_av = $('.ls_av').text();
    data.zz_av = $('.zz_av').text();
    data.dl_av = $('.dl_av').text();

    data.yw_stand_av = $('.yw_stand_av').text();
    data.sx_stand_av = $('.sx_stand_av').text();
    data.yy_stand_av = $('.yy_stand_av').text();
    data.wl_stand_av = $('.wl_stand_av').text();
    data.hx_stand_av = $('.hx_stand_av').text();
    data.sw_stand_av = $('.sw_stand_av').text();
    data.ls_stand_av = $('.ls_stand_av').text();
    data.zz_stand_av = $('.zz_stand_av').text();
    data.dl_stand_av = $('.dl_stand_av').text();

    $.ajax({
        url: '/score',
        data: JSON.stringify(data),
        type: 'POST',
        success: function (result) {
            if(result == 'success')
                window.location.href = '/list';
            else
                alert(result);
        }
    })
}