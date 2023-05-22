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

    axios.post('/api/connect_user_role', data)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
    });
  }
}

const uroleForm = document.querySelector('#connect_user_role-form');
uroleForm.addEventListener('submit', connect_user_roleValidation);
