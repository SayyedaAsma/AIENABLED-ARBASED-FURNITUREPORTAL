$(document).ready(function(){
    $('.viewbtn').click(function(){
        $(this).html($(this).html() == 'view' ? 'modify' : 'view');
    });
});