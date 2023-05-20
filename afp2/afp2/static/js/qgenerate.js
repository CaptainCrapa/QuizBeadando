
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
    if (createbyid.length <= 0) {
      areFieldsValid = false;
      document.querySelector("#creator_error").textContent = "*töltse ki!";
      document.querySelector("#creator").classList.add("form-error-field");
    } else {
      document.querySelector("#creator").classList.remove("form-error-field");
      document.querySelector("#creator_error").textContent = "";
    }
  
    // active validation
    if (active != false && active != true) {
      areFieldsValid = false;
      document.querySelector("#active_error").textContent = "*érvénytelen adat!";
      document.querySelector("#active").classList.add("form-error-field");
    } else {
      document.querySelector("#active").classList.remove("form-error-field");
      document.querySelector("#active_error").textContent = "";
    }
  
    if (areFieldsValid) {
      const data = {
        name: qname,
        active: active,
        created_by: creator
      };
  
      axios.post('/api/create_quiz', data)
          .then(response => {
            console.log(response.data);
          })
          .catch(error => {
            console.log(error);
          });
    }
  }
  
  const qgenerateForm = document.querySelector('#qgenerate-form');
  qgenerateForm.addEventListener('submit', qgenerateValidation);