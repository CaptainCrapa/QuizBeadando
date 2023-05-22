function connect_user_roleValidation(event) {
  event.preventDefault();

    let requester = document.querySelector("#requester").value;
    let username = document.querySelector("#username").value;
    let role = document.querySelector("#role").value;
    let areFieldsValid = true;
  
  // requester length check
  if (requester.length <= 0)
  {
    areFieldsValid = false;
    document.querySelector("#requester_error").textContent = "*töltse ki!";
    document.querySelector("#requester").classList.add("form-error-field");
  }
  else
  {
    document.querySelector("#requester").classList.remove("form-error-field");
    document.querySelector("#requester_error").textContent = "";
  }

  // username length check
  if (username.length <= 0)
  {
    areFieldsValid = false;
    document.querySelector("#username_error").textContent = "*töltse ki!";
    document.querySelector("#username").classList.add("form-error-field");
  }
  else
  {
    document.querySelector("#username").classList.remove("form-error-field");
    document.querySelector("#username_error").textContent = "";
  }

    if (areFieldsValid) {
    const data = {
      user_id: username,
      role_id: role
    };

    axios.post('/api/connect_user_role', data) // Még backendre vár
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

const uroleForm = document.querySelector('#connect_user_role-form');
uroleForm.addEventListener('submit', connect_user_roleValidation);
