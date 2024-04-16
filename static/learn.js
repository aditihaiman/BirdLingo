$(function () {
    $("#next-button").on('click', navigate_next);
    $("#prev-button").on('click', navigate_prev);
    $("#home-learn").on('click', navigate_next);
});


function navigate_next(){
    if(window.location.href.includes('learn')){
        //if at learn/3 go to quiz template
        if(window.location.href.includes('learn/3')){
            //FILL IN WHOEVER IS DOING QUIZ
        }
        else window.location.href = "/learn/" + (Number(learn_data['id'])+1);
    }
    else {
        window.location.href = "/learn/0";
    }
}

function navigate_prev(){
    if(window.location.href.includes('learn')){
        //if at learn/0 go to prev template
        if(window.location.href.includes('learn/0')){
            //FILL IN WHOEVER IS DOING MISCELLANEOUS
        }
        else window.location.href = "/learn/" + (Number(learn_data['id'])-1);
    }
}