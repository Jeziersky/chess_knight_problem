$(".table-solution tr td").filter(function(){
    return $(this).text() === '1'
}).css("background-color", "red");
