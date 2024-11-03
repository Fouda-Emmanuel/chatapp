$(document).on('submit', '#message', function(e){
    e.preventDefault();
    $.ajax({
        type: 'POST',
        url: window.location.href,  // specify your endpoint here
        data: {
            message: $('#msg').val(),
            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
        },
        success: function(response) {
            // Handle success if needed
            $( ".parent" ).load(window.location.href + " .parent" );
        },
        error: function(xhr, status, error) {
            console.error("Error:", error); // Handle error
        }
    });
});

$(document).ready(function(){
    setInterval(function(){
        $( ".message" ).load(window.location.href + " .message" );
    }, 1000);
});
