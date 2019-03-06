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

    $('#ContactForm').submit(function(e) {
        e.preventDefault();
        // Sanitizes email to not contain domain
        let email = $('input[name="email"]').val().split("@")[0] + $( "#ContactForm_Email option:selected" ).text();
        $.ajax({
            url: '/api/contact',
            data: {
                "email": email,
                "message": $('textarea[name="message"]').val()
            },
            type: 'POST',
            dataType: 'json',
            success: function(response) {
                if (response.Status === "Success") {
                    window.alert("Concact send!");
                    window.location.href = '/contact';
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
});
