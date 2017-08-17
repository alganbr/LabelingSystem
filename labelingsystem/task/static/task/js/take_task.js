
/*--------loader script-----------*/
$(document).ready(function(){

    var post_form = document.getElementById('post_form');
    
    $(document.body).on('click',"label.element-animation",function (e) {
        $(this).closest('.row').delay(100).fadeOut();
        $(this).closest('.row').promise().done(function() {
            $(post_form).submit()
        });
    });
});	
