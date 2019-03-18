$(document).ready(function(){
    $('#LoginForm').submit(function(e) {
        e.preventDefault();
        $.ajax({
            url: '/api/login',
            data: {
                "username": $('input[name="username"]').val(),
                "password": $('input[name="password"]').val()
            },
            type: 'POST',
            dataType: 'json',
            success: function(response) {
                if (response.Status === "ErrorUser") {
                    $("#passwordError").slideUp();
                    $("#userError").slideDown();
                }
                else if (response.Status === "ErrorPassword") {
                    $("#userError").slideUp();
                    $("#passwordError").slideDown();
                }
                else if (response.Status === "Success") {
                    window.location.href = '/calendar';
                }
                else {
                    console.log(response);
                }
            },
            error: function(error) {
                console.log(error);
            }
        });
    });
    
    $('.faq-item').click(function(e) {
        let target = $($(this).data('target'));
        if (target.hasClass('collapse')) {
            if (!target.hasClass('show')) {
                $(this).find("i").removeClass('fa-plus-circle').addClass('fa-minus-circle');
        }
            else {
                $(this).find("i").removeClass('fa-minus-circle').addClass('fa-plus-circle');
            }
        }
    });
    
    $('.corset').click(function(e) {
        let checkbox = $(this).find("i");
        if (checkbox.hasClass('fa-square')) {
                checkbox.removeClass('fa-square').addClass('fa-check-square');
                $(this).removeClass('outline-orange').addClass('success');
        }
    });
    
});
