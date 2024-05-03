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

    // Initialize dialogs
    $("#char-info, #spectro-info").dialog({
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

    // Event to open/close dialog on button click
    $("#characteristics, #spectrogram").on("click", function() {
        var targetId = $(this).data("target");
        var targetDialog = $("#" + targetId);
        if (targetDialog.dialog("isOpen")) {
            targetDialog.dialog("close");
        } else {
            targetDialog.dialog("open");
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
        classes: {
            "ui-droppable-hover": "ui-state-hover"
        },
        drop: function(event, ui) {
            var dropZoneBird = $(this).data('bird');
            var draggedBird = ui.draggable.attr('id');

            console.log("Drop Zone expects:", dropZoneBird); // Debugging
            console.log("Dragged Item ID:", draggedBird); // Debugging

            if (draggedBird === dropZoneBird) {
                $(this).append(ui.draggable);
                ui.draggable.position({
                    my: "center",
                    at: "center",
                    of: $(this)
                });
                ui.draggable.css("margin", 0);
                alert("Correct! You placed the " + draggedBird + " in the right zone.");
            } else {
                $(ui.draggable).css({ top: "0px", left: "0px" }); // Reset position
                alert("Incorrect. Try again!");
            }
        }
    });
});

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
    let currentId = parseInt(window.location.pathname.split('/'). pop());
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
