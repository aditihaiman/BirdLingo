$(function () {
    $("#search").on("submit", search);
    $("#add-submit").on("click", validate);
    $("#edit-submit").on("click", validate);
    if (window.location.href.includes("edit")) check_colors_and_size();
    $("#edit-discard").on('click', function(){
        $("#dialog-confirm").dialog('open');
        return false;
    });

    $("#dialog-confirm").dialog({
        autoOpen: false,
        resizable: false,
        height: "auto",
        width: 400,
        modal: true,
        buttons: {
            "Discard changes": function () {
                $(this).dialog("close");
                reset_edit_inputs();
            },
            Cancel: function () {
                $(this).dialog("close");
            }
        }
    });
});

function get_bird_from_inputs() {
    let colors = []
    $(".form-check-input").each(function () {
        if ($(this).prop('checked')) {
            colors.push($(this).attr("name"));
        }
    });
    let bird = {
        "name": $("#name").val(),
        "latin_name": $("#sciname").val(),
        "image": $("#url").val(),
        "colors": colors,
        "description": $("#desc").val(),
        "rarity": $("#rarity").val(),
        "size": $("#size").val(),
        "order": $("#order").val(),
        "family": $("#family").val()
    }
    return bird;
}


function add_bird(event) {
    console.log("Form successfully submitted");
    let bird = get_bird_from_inputs();

    $.ajax({
        type: "POST",
        url: "/add_bird",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(bird),
        success: function (result) {
            let new_bird_link = "/view/" + result[1];
            console.log("Success", result[0]);
            $("#success-message").html(
                "New bird successfully added!<br>See it here: <a href=\'" + new_bird_link + "\'class=link>" + $("#name").val() + "</a>"
            );
            //reset form
            $("input")
                .val('')
                .prop('checked', false);
            $("select").val('sparrow');
            $("textarea").val('');
        },
        error: function (request, status, error) {
            console.log("Error: could not save new bird");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}

function search(event) {
    event.preventDefault();
    let search_term = $("#search_input").val().trim();
    if (search_term.length != 0) {
        window.location.href = '/search_results/' + search_term;
        // display_search_results();
    }
    else {
        $("#search_input").val("");
    }

}


function validate(event) {
    event.preventDefault();

    let valid = true;

    if ($("#family").val().trim().length == 0) {
        $("#family-error").html("Please enter a valid name");
        $("#family").focus();
        valid = false;
    }
    else $("#family-error").html("");


    if ($("#order").val().trim().length == 0) {
        $("#order-error").html("Please enter a valid order");
        $("#order").focus();
        valid = false;
    }
    else $("#order-error").html("");

    let r = $("#rarity").val();
    if (!$.isNumeric(r) || parseInt(r) != parseFloat(r) || parseInt(r) < 0 || parseInt(r) > 9) {
        $("#rarity-error").html("Please enter a valid integer between 0 and 9 inclusive");
        $("#rarity").focus();
        valid = false;
    }
    else $("#rarity-error").html("");

    //validate colors
    let valid_color = false;
    $(".form-check-input").each(function () {
        valid_color = valid_color || $(this).prop('checked');
    });
    if (!valid_color) {
        $("#color-error").html("Please check at least one color");
        valid = false;
    }
    else $("#color-error").html("");


    if ($("#desc").val().trim().length == 0) {
        $("#desc-error").html("Please enter a valid description");
        $("#desc").focus();
        valid = false;
    }
    else $("#desc-error").html("");

    try {
        $("#url-error").html("");
        url = new URL($("#url").val());
    } catch (error) {
        $("#url-error").html("Please enter a valid url");
        $("#url").focus();
        valid = false;
    }

    if ($("#sciname").val().trim().length == 0) {
        $("#sciname-error").html("Please enter a valid scientific name");
        $("#sciname").focus();
        valid = false;
    }
    else $("#sciname-error").html("");

    if ($("#name").val().trim().length == 0) {
        $("#name-error").html("Please enter a valid name");
        $("#name").focus();
        valid = false;
    }
    else $("#name-error").html("");

    if (valid) {
        if (window.location.href.includes("add")) add_bird(event);
        if (window.location.href.includes("edit")) edit_bird(event);
    }
    // else event.preventDefault();
}


function check_colors_and_size() {
    $(".form-check-input").each(function () {
        if (bird["colors"].includes($(this).attr("name"))) {
            $(this).prop('checked', true);
        }
    });
    $("select").val(bird["size"]);
}

function reset_edit_inputs() {
    $("#name").val(bird["name"]);
    $("#sciname").val(bird["latin_name"]);
    $("#url").val(bird["image"]);
    $("#desc").html(bird["description"]);
    check_colors_and_size();
    $("#rarity").val(bird["rarity"]);
    $("#order").val(bird["order"]);
    $("#family").val(bird["family"]);
}

function edit_bird(event) {
    console.log("Edit form successfully submitted");
    let updated_bird = get_bird_from_inputs();

    $.ajax({
        type: "POST",
        url: "/edit_bird",
        dataType: "json",
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify([updated_bird, id]),
        success: function (result) {
            let new_bird_link = "/view/" + result[1];
            console.log("Successful update", result[0]);
            window.location.href = new_bird_link;
        },
        error: function (request, status, error) {
            console.log("Error: could not update bird");
            console.log(request);
            console.log(status);
            console.log(error);
        }
    });
}