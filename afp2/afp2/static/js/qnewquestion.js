
document.querySelector('#qnewquestion-form').addEventListener("submit", (event) => {

    event.preventDefault();
  
    let qquestion = document.querySelector("#qquestion").value;
    let qqture = document.querySelector("#qquestion_true");
    let qqfalse = document.querySelector("#qquestion_false");
    let areFieldsValid = true;
  
    // question length check
    if (qquestion.length <= 0) {
        areFieldsValid = false;
        document.querySelector("#qquestion_error").textContent = "*töltse ki!";
        document.querySelector("#qquestion").classList.add("form-error-field");
    }
    else {
        document.querySelector("#qname").classList.remove("form-error-field");
        document.querySelector("#qquestion").textContent = "";
    }
    // radio button check
    if (!qqture.checked && !qqfalse.checked) { 
        areFieldsValid = false;
        document.querySelector("#qquestionanswer_error").textContent = "*válasszon!";
    }
    else {
        document.querySelector("#qquestionanswer_error").textContent = "";
    }

    if (areFieldsValid) {
        
        let qanswer = (qqture.checked) ? qqture.value : qqfalse.value;

        const data = {
            question: qquestion,
            answer: qanswer
        };
  
        axios.post('/api/create_question', data)
            .then(response => console.log(response.data))
            .catch(error => console.log(error));
    }
});