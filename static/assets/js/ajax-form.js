(function ($) {
    'use strict';
    var form = $('.contact-form'),
        message = $('.messenger-box-contact__msg'),
        form_data;

    // Success function
    function done_func(response) {
        message.fadeIn().removeClass('alert-danger').addClass('alert-success');
        message.text("Your message was sent successfully."); // Başarılı mesajı burada ayarlanıyor
        setTimeout(function () {
            message.fadeOut();
        }, 3000);
        form.find('input:not([type="submit"]), textarea').val('');
    }

    // Fail function
    function fail_func(data) {
        var error_message = "An error occurred. Please try again."; // Genel hata mesajı

        if (data.responseJSON && data.responseJSON.error_message) {
            // Eğer sunucudan özel bir hata mesajı dönerse onu kullan
            error_message = data.responseJSON.error_message;
        }

        message.fadeIn().removeClass('alert-success').addClass('alert-danger');
        message.text(error_message);
        setTimeout(function () {
            message.fadeOut();
        }, 3000);
        form.find('input:not([type="submit"]), textarea').val('');
    }

    form.submit(function (e) {
        e.preventDefault();

        const message = document.getElementById('required-msg');
        const fullName = document.getElementById("full-name");
        const email = document.getElementById("email");
        const subject = document.getElementById("subject");

        if (!fullName.value || !email.value) {
            message.classList.add('show');
            fullName.classList.add("invalid");
            console.log('false');
            return false;
        }
        message.classList.remove('show');

        form_data = $(this).serialize();
        $.ajax({
            type: 'POST',
            url: form.attr('action'),
            data: form_data
        })
            .done(done_func)
            .fail(fail_func);
    });

})(jQuery);
