$(function(){
    /* navbar li active */
    $('#navbar li').each(function (){
        $li_a = $(this).find('a');
        $(this).toggleClass('active', location.pathname.indexOf($li_a.attr('href')) > -1);
    });
})
