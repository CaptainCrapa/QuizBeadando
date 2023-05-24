let quizIdLink = document.getElementById("quizId");
    quizIdLink.style.display = "none";
function createQuestionAndAddToQuiz(event) {
    event.preventDefault();

  let question = document.querySelector("#question").value;
  let answerNum = document.querySelector("#answer").value;
  let answer = false;
  let activeNum = document.querySelector("#active").value;
  let active= false;
  let areFieldsValid = true;

    // question length validation
    if (question.length <= 0) {
      areFieldsValid = false;
      document.querySelector("#question_error").textContent = "*töltse ki!";
      document.querySelector("#question").classList.add("form-error-field");
    } else {
      document.querySelector("#question").classList.remove("form-error-field");
      document.querySelector("#question").textContent = "";
    }

    // answer validation
    if (answerNum == 1) {
        answer = true;
    }

    if (answer == true || answer == false) {
      document.querySelector("#answer").classList.remove("form-error-field");
      document.querySelector("#answer_error").textContent = "";
    } else {
      areFieldsValid = false;
      document.querySelector("#answer_error").textContent = "*érvénytelen adat!";
      document.querySelector("#answer").classList.add("form-error-field");
    }

    // active validation
    if (activeNum == 1) {
        active = true;
    }

    if (active == true || active == false) {
      document.querySelector("#active").classList.remove("form-error-field");
      document.querySelector("#active_error").textContent = "";
    } else {
      areFieldsValid = false;
      document.querySelector("#active_error").textContent = "*érvénytelen adat!";
      document.querySelector("#active").classList.add("form-error-field");
    }

    if (areFieldsValid) {
      const data = {
        question: question,
        answer: answer,
        active: active
      }


      axios.post('/api/create_question', data)
      .then(function(response) {
        addQuestionToQuiz(response.data);
      })
      .catch(error => {
      if (error.response) {
        let errorMessage = error.response.data;
        document.querySelector('#error').textContent = errorMessage;
        document.querySelector("#success").textContent = "";
      } else {
        console.log(error);
        document.querySelector('#error').textContent = "Hiba. További információ a konzolban!";
        document.querySelector("#success").textContent = "";
      }
      });
    };

    function addQuestionToQuiz(questionId) {

        let quizId = document.getElementById('quizId').value;
        const data = {
            quiz_id: quizId,
            question_id: questionId
        }

        axios.post('/api/add_question_to_quiz', data)
            .then(function (response) {
                document.querySelector("#success").textContent = response.data;
                document.querySelector("#error").textContent = "";
                setTimeout(function () {
                location.reload();
                }, 1500);
            })
            .catch(error => {
                if (error.response) {
                    let errorMessage = error.response.data;
                    document.querySelector('#error').textContent = errorMessage;
                    document.querySelector("#success").textContent = "";
                } else {
                    console.log(error);
                    document.querySelector('#error').textContent = "Hiba. További információ a konzolban!";
                    document.querySelector("#success").textContent = "";
                }
            });
    }
}

function finishQuiz() {
    window.location.href = '/api/finish_quiz';
}

const qquestionForm = document.querySelector('#qquestion-form');
qquestionForm.addEventListener('submit', createQuestionAndAddToQuiz);
