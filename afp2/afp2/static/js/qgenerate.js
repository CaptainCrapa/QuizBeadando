
function qgenerateValidation(event) {
    event.preventDefault();
  
    let active = document.querySelector("#active").value;
    let qname = document.querySelector("#qname").value;
    let creator = document.querySelector("#creator").value;
    let areFieldsValid = true;
  
  // qname length check
    if (qname.length <= 0) {
      areFieldsValid = false;
      document.querySelector("#qname_error").textContent = "*töltse ki!";
      document.querySelector("#qname").classList.add("form-error-field");
    } else {
      document.querySelector("#qname").classList.remove("form-error-field");
      document.querySelector("#qname_error").textContent = "";
    }
  
    // creator length check
    if (creator.length <= 0) {
      areFieldsValid = false;
      document.querySelector("#creator_error").textContent = "*töltse ki!";
      document.querySelector("#creator").classList.add("form-error-field");
    } else {
      document.querySelector("#creator").classList.remove("form-error-field");
    }
  
    // active validation
    if (active == "true" || active == "false") {
      document.querySelector("#active").classList.remove("form-error-field");
      document.querySelector("#active_error").textContent = "";
    } else {
      areFieldsValid = false;
      document.querySelector("#active_error").textContent = "*érvénytelen adat!";
      document.querySelector("#active").classList.add("form-error-field");
    }
  
    if (areFieldsValid) {
      const data = {
        name: qname,
        active: active,
        created_by: creator
      };
  
      axios.post('/api/create_quiz', data)
          .then(response => {
            document.querySelector("#success").textContent = response.data;
            document.querySelector("#error").textContent = "";
          })
          .catch(error => {
          if (error.response) {
            var errorMessage = error.response.data;
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
  
  const qgenerateForm = document.querySelector('#qgenerate-form');
  qgenerateForm.addEventListener('submit', qgenerateValidation);