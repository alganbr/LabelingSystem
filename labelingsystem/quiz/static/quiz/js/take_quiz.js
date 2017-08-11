
/*--------loader script-----------*/
$(document).ready(function(){

    var count = 0;
    var quiz_form = document.getElementById('quiz_form');
    var rows = $(quiz_form).find('div.row');

    $(document.body).on('click', "div.start_quiz", function (e) {
        var prolog = document.getElementById('prolog');
        $(prolog).hide();

        // show current row
        var curr = $(rows).get(count);
        $(curr).show();
    })

    var num_questions = window.num_questions || null
    
    $(document.body).on('click',"label.element-animation",function (e) {
        count++;
        $(this).closest('.row').delay(100).fadeOut();
        curr = $(rows).get(count);
        $(curr).show();

        if(count >= num_questions) {
            console.log("complete");
            $('input[type=radio]').on('change', function() {
                $(this).closest("form").submit();
            });
        }
    });
});	

