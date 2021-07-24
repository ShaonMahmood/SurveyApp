function buildSurvey() {
    // variable to store the HTML output
    const output = [];
    questions.forEach(
        (currentQuestion, questionNumber) => {

            // variable to store the list of possible answers
            const answers = [];
            if (currentQuestion.type === "text") {
                answers.push(`<input type="text" name="question${questionNumber}" placeholder="${currentQuestion.placeholder}">`);
            } else if (currentQuestion.type === "radio") {
                for (const element of currentQuestion.answer_options) {
                    // console.log(element);
                    answers.push(
                        `<label>
                <input type="radio" name="question${questionNumber}" value="${element.value}">
                ${element.text}
              </label><br>`
                    );
                }
            } else if (currentQuestion.type === "checkbox") {
                for (const element of currentQuestion.answer_options) {
                    // console.log(element);
                    answers.push(
                        `<label>
                <input type="checkbox" class="qCheckbox" name="question${questionNumber}" value="${element.value}">
                ${element.text}
              </label><br>`
                    );
                }
            }
            output.push(
                `<div class="slide">
                 <div class="question"> <h3 style="color: #006b1b"> <span style="color: #ba2121">Question ${currentQuestion.order}</span>: ${currentQuestion.text}</h3></div>
                 <div class="answers"> ${answers.join('')} </div>
                 </div>`
            );
        }
    );
    // finally combine our output list into one string of HTML and put it on the page

    surveyContainer.innerHTML = output.join('');



}

const sendData = (answer_list) => {
    const data = {};
    data['csrfmiddlewaretoken'] = csrf[0].value;
    data['answer_list'] = JSON.stringify(answer_list);
    console.log(data);
    $.ajax({
        url: `${url}save/`,
        type: "POST",
        data: data,
        dataType: "json",
        success: function (response) {
            if (response.status === "success") {
                console.log(`Response: ${response.message}`);
                alert(response.message);
                window.location.href = "/survey/";
            }
        },
        error: function (error) {
            console.log(`Error :${error}`);
        }
    });
}

function showResults() {

    // gather answer containers from our survey
    const answerContainers = surveyContainer.querySelectorAll('.answers');
    let survey_answers = [];
    // for each question...
    questions.forEach((currentQuestion, questionNumber) => {
            // find selected answer
            const answerContainer = answerContainers[questionNumber];
            console.log(answerContainer);
            if (currentQuestion.type === "text") {
                const selector = `input[name=question${questionNumber}]`;
                const userAnswer = (answerContainer.querySelector(selector) || {}).value;
                let single_obj = {};
                single_obj['question'] = currentQuestion.id;
                single_obj['answer'] = userAnswer;
                survey_answers.push(single_obj);
                console.log(single_obj);
            } else {
                if (currentQuestion.type === "radio") {
                    const selector = `input[name=question${questionNumber}]:checked`;
                    const userAnswer = (answerContainer.querySelector(selector) || {}).value;

                    let single_obj = {};
                    single_obj['question'] = currentQuestion.id;
                    single_obj['answer'] = userAnswer;
                    survey_answers.push(single_obj);
                    console.log(single_obj);
                } else {
                    let array = [];
                    $(`input:checkbox[name=question${questionNumber}]:checked`).each(function () {
                        array.push($(this).val());
                    });
                    let userAnswer = array.join(",");

                    let single_obj = {};
                    single_obj['question'] = currentQuestion.id;
                    single_obj['answer'] = userAnswer;
                    survey_answers.push(single_obj);
                    console.log(single_obj);
                }
            }
        }
    );
    console.log(`Survey_answers: ${survey_answers}`);

    sendData(survey_answers);

}

function showSlide(n) {
    slides[currentSlide].classList.remove('active-slide');
    slides[n].classList.add('active-slide');
    currentSlide = n;
    if (currentSlide === 0) {
        previousButton.style.display = 'none';
    } else {
        previousButton.style.display = 'inline-block';
    }
    if (currentSlide === slides.length - 1) {
        nextButton.style.display = 'none';
        submitButton.style.display = 'inline-block';
    } else {
        nextButton.style.display = 'inline-block';
        submitButton.style.display = 'none';
    }
}

function showNextSlide() {
    showSlide(currentSlide + 1);
}

function showPreviousSlide() {
    showSlide(currentSlide - 1);
}

const surveyContainer = document.getElementById('survey');
const resultsContainer = document.getElementById('results');
const submitButton = document.getElementById('submit');
const url = window.location.href;
const csrf = document.getElementsByName('csrfmiddlewaretoken');

// display survey questions right away
buildSurvey();

// Pagination
const previousButton = document.getElementById("previous");
const nextButton = document.getElementById("next");
const slides = document.querySelectorAll(".slide");

let currentSlide = 0;

showSlide(currentSlide);

// on submit, show results
submitButton.addEventListener('click', showResults);
previousButton.addEventListener("click", showPreviousSlide);
nextButton.addEventListener("click", showNextSlide);
