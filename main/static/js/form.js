$(function() {

    var form = $('#ajax-contact');
    var formMessages = $('#form-messages');

    $(form).submit(function(e) {
        e.preventDefault();

        var formData = $(form).serialize();

        $.ajax({
            type: 'POST',
            url: $(form).attr('action'),
            data: formData,
            headers: { 'X-CSRFToken': $('input[name=csrfmiddlewaretoken]').val() }
        })
        .done(function(response) {
            formMessages.removeClass('bg-danger').addClass('bg-success');
            formMessages.text('Your message successfully sent');
            $('#name, #email, #message').val('');
        })
        .fail(function(data) {
            formMessages.removeClass('bg-success').addClass('bg-danger');
            formMessages.text('Error submitting form');
        });

    });

});
