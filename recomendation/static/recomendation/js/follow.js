$(document).ready(function(){

    templates = {
        'suggestion': _.template($("#template-suggestion").html())
    };

    $.ajax({
        url: "suggestion",
        success:function(data, xsr){
            renderSuggestion(data);
        }
    })
});

removeSuggestion = function(user){
    var user = $(user).parent().parent();
    user.fadeOut();
    user.remove();
}

renderSuggestion = function(users){
    $('.sugestion').html(templates.suggestion({users:users}));
}