$(function(){
    /* prepend arrow symbol to every p in main_content */
    $('div.work_content p').each(function (){
        $(this).prepend('&#10140; ');
    });

    /* prepend briefcase icon to every h4 in period div */
    $('div.period h4').each(function (){
        $(this).prepend('<i class="glyphicon glyphicon-briefcase"></i>');
    });

    /* prepend calendar icon to every p in period div */
    $('div.period p').each(function (){
        $(this).prepend('<i class="glyphicon glyphicon-calendar"></i>');
    });
})
