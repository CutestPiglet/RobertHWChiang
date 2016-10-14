$(function(){
    /* prepend check symbol to every p in main_content */
    $('div#main_content p').each(function (){
        $(this).prepend('&#10004; ');
    });
})
