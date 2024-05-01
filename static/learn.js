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
});


function navigate_next() {
    let currentId = parseInt(window.location.pathname.split('/').pop());
    if (window.location.href.includes('learn')) {
        if (window.location.href.includes('learn_checkpoint')) {
            // Redirect to the second learning page
            window.location.href = "/learn/4";
        } else if (window.location.href.includes('learn/3')) {
            // Redirect to the checkpoint page after the second learning page
            window.location.href = "/learn_checkpoint";
        } else if (currentId === 5) { // Assuming 4 is the ID of the last learning slide
            // Redirect to the quiz
            window.location.href = "/quiz/0";
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
        } else if (window.location.href.includes('learn/4')) {
            window.location.href = '/learn_checkpoint';
        } else {
            window.location.href = "/learn/" + (currentId - 1);
        }
    }
}
