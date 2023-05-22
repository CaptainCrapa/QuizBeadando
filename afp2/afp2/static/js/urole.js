function connect_user_roleValidation(event) {
  event.preventDefault();

    let username = document.querySelector("#username").value;
    let role = document.querySelector("#role").value;
    let areFieldsValid = true;

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
      user_name: username,
      role_id: role
    };

    axios.post('/api/connect_user_role', data)
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
