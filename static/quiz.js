$(function () {
    $("#next-button").on('click', navigate_next);
    $("#prev-button").on('click', navigate_prev);
    $("#home-quiz").on('click', navigate_next);
    $("#home-learn").on('click', go_to_learn);
    $(".submit-button").on('click', submit);

    $(".question").on('click', function(){
        $("#spectro-info").toggleClass('d-none');
    });
    $("#spectrogram").on('click', function(){
        $("#spectro-info").toggleClass('d-none');
    });
    $("#characteristics").on('click', function(){
        $("#char-info").toggleClass('d-none');
    });

});

function navigate_next() {
    if (!window.location.href.includes('quiz')) {
        $.ajax({
            type: "POST",
            url: "/clear_total",
            success: function(response) {
                console.log("Total cleared!");
            },
            error: function(xhr, status, error) {
                console.error("Error updating variable:", error);
            }
        });
    }

    if (window.location.href.includes('quiz')) {
        if (window.location.href.includes('quiz/2')) {
            //FILL IN WHOEVER IS DOING QUIZ
            window.location.href = "/results";
        }
        else window.location.href = "/quiz/" + (Number(quiz_data['id']) + 1);
    }
    else {
        window.location.href = "/quiz/0";
    }
}

function navigate_prev() {
    if (window.location.href.includes('quiz')) {
        //if at quiz/0 go to prev template
        if (window.location.href.includes('quiz/0')) {
            //FILL IN WHOEVER IS DOING MISCELLANEOUS
        }
        else window.location.href = "/quiz/" + (Number(quiz_data['id']) - 1);
    }
}

function go_to_learn() {
    window.location.href = "/learn/0"
}

function submit() {
    var buttonId = $(this).attr("id");
    if(buttonId == "submit-button-0"){
        var checkedValues = [];

        // Loop through each checkbox within the checkboxContainer
        $("#checkboxContainer input[type='checkbox']").each(function() {
            // If the checkbox is checked, add its value to the array
            if ($(this).is(":checked")) {
                checkedValues.push($(this).val());
            }
        });

        // Output the checked values to the console
        console.log("Checked values:", checkedValues);

        let newValue = 0;

        if(checkedValues.length == 2 && checkedValues.includes("harsh") && checkedValues.includes("falling pitch")){
            $.ajax({
                type: "POST",
                url: "/update_total",
                data: { variable: newValue },
                success: function(response) {
                    console.log("Variable updated successfully!");
                },
                error: function(xhr, status, error) {
                    console.error("Error updating variable:", error);
                }
            });
            $("#quiz-feedback").empty()
            $("#quiz-feedback").append("Correct! &check;");

        }
        else{
            $("#quiz-feedback").empty()
            $("#quiz-feedback").append("Incorrect &cross;");
        }
    }
    else if(buttonId == "submit-button-1"){
        var checkedValues = [];

        // Loop through each checkbox within the checkboxContainer
        $("#checkboxContainer input[type='checkbox']").each(function() {
            // If the checkbox is checked, add its value to the array
            if ($(this).is(":checked")) {
                checkedValues.push($(this).val());
            }
        });

        // Output the checked values to the console
        console.log("Checked values:", checkedValues);

        let newValue = 1;

        if(checkedValues.length == 1 && checkedValues.includes("Northern Cardinal")){
            $.ajax({
                type: "POST",
                url: "/update_total",
                data: { variable: newValue },
                success: function(response) {
                    console.log("Variable updated successfully!");
                },
                error: function(xhr, status, error) {
                    console.error("Error updating variable:", error);
                }
            });
            $("#quiz-feedback").empty()
            $("#quiz-feedback").append("Correct! &check;");
        }
        else{
            $("#quiz-feedback").empty()
            $("#quiz-feedback").append("Incorrect &cross;");
        }
    }
    else if(buttonId == "submit-button-2"){
        var draggedValues = [];

        // Assuming you have a container with draggable elements
        $(".draggable.dropped").each(function() {
            // Capture the value or attribute of the dragged element
            var value = $(this).text(); // Change this to capture the value or attribute you need
            draggedValues.push(value.trim());
        });

        // Output the values to the console
        console.log("Dragged values:", draggedValues);

        let newValue = 2;

        if(draggedValues.length == 2 && draggedValues[0] == "Red-Tailed Hawk" && draggedValues[1] == "American Robin"){
            $.ajax({
                type: "POST",
                url: "/update_total",
                data: { variable: newValue },
                success: function(response) {
                    console.log("Variable updated successfully!");
                },
                error: function(xhr, status, error) {
                    console.error("Error updating variable:", error);
                }
            });
            $("#quiz-feedback").empty()
            $("#quiz-feedback").append("Correct! &check;");
        }
        else{
            $("#quiz-feedback").empty()
            $("#quiz-feedback").append("Incorrect &cross;");
        }
    }
}

$( function() {
    $( ".draggable" ).draggable({
        revert: "invalid",
    });
    $( ".droppable" ).droppable({
        over: function (event, ui) {
            $(this).addClass("ui-state-hover");
        },

        out: function (event, ui) {
            $(this).removeClass("ui-state-hover");
        },
      drop: function( event, ui ) {
        ui.draggable.addClass("dropped");
        }
    });
  } );

$(document).ready(function() {
    // Check if the current page is a quiz page
    if (window.location.href.includes('results')) {
        // Retrieve the variable value from the server using AJAX
        $.ajax({
            type: "GET",
            url: "/get_total",
            success: function(response) {
                var total = response.variable;
                console.log("Variable value:", total);
                // Update HTML content with the variable value
                $("#variableContainer").text(total + " out of 3");
            },
            error: function(xhr, status, error) {
                console.error("Error retrieving variable:", error);
            }
        });
    }
});