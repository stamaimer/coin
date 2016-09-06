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
        var sum3 = parseInt($(this).find('td:eq(2)').text()) + parseInt($(this).find('td:eq(3)').text()) + parseInt($(this).find('td:eq(4)').text());
        var sum5 = parseInt($(this).find('td:eq(2)').text()) + parseInt($(this).find('td:eq(3)').text()) + parseInt($(this).find('td:eq(4)').text()) + parseInt($(this).find('td:eq(5)').text()) + parseInt($(this).find('td:eq(6)').text());
        $(this).find('td:eq(11)').text(sum3);
        $(this).find('td:eq(14)').text(sum5);
        sortBy3();
        sortBy5();
    });
    calcAverage()
}


function calcAverage() {
    for(var i = 1 ;i <= 9;i++){
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
        .find('td:eq(11)')
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
        score.wl = $(this).find('.wl').text();
        score.hx = $(this).find('.hx').text();
        score.sw = $(this).find('.sw').text();
        score.ls = $(this).find('.ls').text();
        score.zz = $(this).find('.zz').text();
        score.dl = $(this).find('.dl').text();
        score.sum_3 = $(this).find('.sum_3').text();
        score.class_rank_3 = $(this).find('.class_rank_3').text();
        score.grade_rank_3 = $(this).find('.grade_rank_3').text();
        score.sum_5 = $(this).find('.sum_5').text();
        score.class_rank_5 = $(this).find('.class_rank_5').text();
        score.grade_rank_5 = $(this).find('.grade_rank_5').text();
        data.scores.push(score);
    });
    data.yw_av = $('.yw-av').text();
    data.sx_av = $('.sx-av').text();
    data.yy_av = $('.yy-av').text();
    data.wl_av = $('.wl-av').text();
    data.hx_av = $('.hx-av').text();
    data.sw_av = $('.sw-av').text();
    data.ls_av = $('.ls-av').text();
    data.zz_av = $('.zz-av').text();
    data.dl_av = $('.dl-av').text();
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