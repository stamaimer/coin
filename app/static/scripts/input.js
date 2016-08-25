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
    $('#calc').click(function () {
        autoCalc();
    });
    $('thead th').clickToggle(function (evt) {
        var tmp = $('.score').sort(sortBy($(this).index()));
        //$('#score tbody').empty();
        //tmp.each(function (index) {
        //    $('#score tbody').append($(this));
        //})
        tmp.detach().appendTo('#score tbody');
    }, function (evt) {
        var tmp = $('.score').sort(sortRevertBy($(this).index()));
        //$('#score tbody').empty();
        //tmp.each(function (index) {
        //    $('#score tbody').append($(this));
        //})
        tmp.detach().appendTo('#score tbody');
    })
});

function autoCalc() {
    $('.score').each(function (index, value) {
        var sum3 = parseInt($(this).find('td:eq(1)').text()) + parseInt($(this).find('td:eq(2)').text()) + parseInt($(this).find('td:eq(3)').text());
        var sum5 = parseInt($(this).find('td:eq(1)').text()) + parseInt($(this).find('td:eq(2)').text()) + parseInt($(this).find('td:eq(3)').text()) + parseInt($(this).find('td:eq(4)').text()) + parseInt($(this).find('td:eq(5)').text());
        $(this).find('td:eq(10)').text(sum3);
        $(this).find('td:eq(13)').text(sum5);
        sortBy3();
        sortBy5();
    });
}
function sortBy3() {
    $('.score')
        .find('td:eq(10)')
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
        .find('td:eq(13)')
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
