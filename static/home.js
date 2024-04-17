$(function () {
    $("#home-learn").on('click', navigate_next_learn);
    $("#home-quiz").on('click', navigate_next_quiz);

});

function navigate_next_learn() {

        window.location.href = "/learn/0";
    
}

function navigate_next_quiz() {
    if (window.location.href.includes('quiz')) {
        //if at learn/3 go to quiz results
        if (window.location.href.includes('quiz/2')) {
            //FILL IN WHOEVER IS DOING QUIZ
            alert("done, go to results")
        }
        else window.location.href = "/quiz/" + (Number(quiz_data['id']) + 1);
    }
    else {
        window.location.href = "/quiz/0";
    }
}