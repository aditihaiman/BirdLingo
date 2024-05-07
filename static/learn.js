$(function () {
    // Navigation buttons
    $("#next-button").on('click', navigate_next);
    $("#prev-button").on('click', navigate_prev);
    $("#home-learn").on('click', navigate_next);

    // Toggling information dialogs
    $("#spectrogram").on('click', function() {
        $("#spectro-info").toggleClass('d-none');
    });
    $("#characteristics").on('click', function() {
        $("#char-info").toggleClass('d-none');
    });

    $( "#char-info" ).dialog({
        autoOpen: false,
        draggable: true,
        show: {
          effect: "blind",
          duration: 500
        },
        hide: {
          effect: "blind",
          duration: 500
        }
      });
   
    $( "#characteristics" ).on( "click", function() {
        if($("#char-info").dialog("isOpen")){
            $( "#char-info" ).dialog( "close" );
        }
        else{
            $( "#char-info" ).dialog( "open" );
        }
    });

    $( "#spectro-info" ).dialog({
        autoOpen: false,
        draggable: true,
        show: {
          effect: "blind",
          duration: 500
        },
        hide: {
          effect: "blind",
          duration: 500
        }
    });

    $( "#spectrogram" ).on( "click", function() {
        if($("#spectro-info").dialog("isOpen")){
            $( "#spectro-info" ).dialog( "close" );
        }
        else{
            $( "#spectro-info" ).dialog( "open" );
        }
    });

    // Drag and Drop functionality
    $(".draggable").draggable({
        revert: "invalid",
        start: function() {
            $(this).css("opacity", 0.5);
        },
        stop: function() {
            $(this).css("opacity", 1);
        }
    });

    $(".droppable").droppable({
        accept: ".draggable",
        drop: function(event, ui) {
            var dropZoneBird = $(this).data('bird');
            var draggedBird = ui.draggable.attr('id');

            if (draggedBird === dropZoneBird) {
                $(this).append(ui.draggable);
                ui.draggable.position({
                    my: "center",
                    at: "center",
                    of: $(this)
                });
                ui.draggable.css("margin", 0);
                provideFeedback(true);
            } else {
                $(ui.draggable).css({ top: "0px", left: "0px" }); // Reset position
                provideFeedback(false);
            }
        }
    });
});

function provideFeedback(isCorrect) {
    var feedbackElement = $("#learn-feedback");
    feedbackElement.empty();

    if (isCorrect) {
        feedbackElement.append("<p>Correct! &check;</p>");
    } else {
        feedbackElement.append("<p>Incorrect &cross;. Please try again!</p>");
    }
}

function navigate_next() {
    let currentId = parseInt(window.location.pathname.split('/').pop());
    if (window.location.href.includes('learn')) {
        if (window.location.href.includes('learn_checkpoint')) {
            window.location.href = "/learn/4";
        } else if (window.location.href.includes('learn/3')) {
            window.location.href = "/learn_checkpoint";
        } else if (currentId === 5) { // Assuming 4 is the last learning slide
            window.location.href = "/transition";
        } else {
            window.location.href = "/learn/" + (currentId + 1);
        }
    } else {
        window.location.href = "/learn/0";
    }
}

function navigate_prev() {
    let currentId = parseInt(window.location.pathname.split('/').pop());
    if (window.location.href.includes('learn')) {
        if (window.location.href.includes('learn/0')) {
            // Fill in whoever is handling miscellaneous
        } else if (window.location.href.includes('learn/4')) {
            window.location.href = '/learn_checkpoint';
        } else {
            window.location.href = "/learn/" + (currentId - 1);
        }
    }
}
