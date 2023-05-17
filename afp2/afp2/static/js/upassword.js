function modifyUserPasswordValidation(event) {
  event.preventDefault();

    let requester = document.querySelector("#requester").value;
    let username = document.querySelector("#username").value;
    let password = document.querySelector("#password").value;
    let confirmPassword = document.querySelector("#confirm-password").value;
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

  // password length check
  if (password.length <= 0) 
  {
    areFieldsValid = false;
    document.querySelector("#password_error").textContent = "*töltse ki!";
    document.querySelector("#password").classList.add("form-error-field");
  }
  else
  {
    document.querySelector("#password").classList.remove("form-error-field");
    document.querySelector("#password_error").textContent = "";
  }

  // password confirmation check
  if (confirmPassword != password) 
  {
    areFieldsValid = false;
    document.querySelector("#confirm-password_error").textContent = "*a jelszavak nem egyeznek!";
    document.querySelector("#confirm-password").classList.add("form-error-field");
  }
  else
  {
    document.querySelector("#confirm-password").classList.remove("form-error-field");
    document.querySelector("#confirm-password_error").textContent = "";
  }

  if (areFieldsValid) {
    const data = {
      requester: requester,
      username: username,
      newPassword: password,
    };

    axios.post('/api/modification_pw', data)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
    });
  }
}

const upasswordForm = document.querySelector('#modifyUserPassword-form');
upasswordForm.addEventListener('submit', modifyUserPasswordValidation);
