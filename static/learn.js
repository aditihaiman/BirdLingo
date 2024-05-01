$(function () {
    $("#next-button").on('click', navigate_next);
    $("#prev-button").on('click', navigate_prev);
    $("#home-learn").on('click', navigate_next);
    $("#spectrogram").on('click', function(){
        $("#spectro-info").toggleClass('d-none');
    });
    $("#characteristics").on('click', function(){
        $("#char-info").toggleClass('d-none');
    });

});


function navigate_next() {
    let currentId = parseInt(window.location.pathname.split('/').pop());
    if (window.location.href.includes('learn')) {
        if (window.location.href.includes('learn_checkpoint')) {
            // Redirect to the second learning page
            window.location.href = "/learn/2";
        } else if (window.location.href.includes('learn/2')) {
            // Redirect to the checkpoint page after the second learning page
            window.location.href = "/learn_checkpoint";
        } else if (currentId === 3) { // Assuming 4 is the ID of the last learning slide
            // Redirect to the quiz
            window.location.href = "/transition";
        } else {
            // Navigate to the next learning slide
            window.location.href = "/learn/" + (currentId + 1);
        }
    } else {
        window.location.href = "/learn/0";
    }
}


function navigate_prev() {
    let currentId = parseInt(window.location.pathname.split('/').pop());
    if (window.location.href.includes('learn')) {
        // If at learn/0, go to prev template (fill in as needed)
        if (window.location.href.includes('learn/0')) {
            // FILL IN WHOEVER IS DOING MISCELLANEOUS
        } else {
            window.location.href = "/learn/" + (currentId - 1);
        }
    }
}
