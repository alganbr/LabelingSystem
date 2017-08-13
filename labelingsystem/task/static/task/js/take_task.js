
/*--------loader script-----------*/
$(document).ready(function(){

    var count = 0;
    var task_form = document.getElementById('task_form');

    // bind form
    $(task_form).ajaxForm(function() {
        alert("Thank you for your comment!");
        console.log("submitting");
        return false;
    });

    $('#task_form').on('submit', function (e) {
        e.preventDefault();
        console.log("form submitted");
        create_post();
    });

    var rows = $(task_form).find('div.row');

    // show current row
    var curr = $(rows).get(count);
    $(curr).show();

    var num_questions = window.num_questions || null
    
    $(document.body).on('click',"label.element-animation",function (e) {
        count++;
        $(this).closest('.row').delay(100).fadeOut();
        $(this).closest('.row').promise().done(function() {
            curr = $(rows).get(count);
            $(curr).show();
        });

        if(count >= num_questions) {
            console.log("complete");
            $('input[type=radio]').on('change', function() {
                $(this).closest("form").submit();
            });
        }
    });
});	

