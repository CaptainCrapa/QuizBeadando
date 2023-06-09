function registrationValidation(event) {
  event.preventDefault();

  let fullname = document.querySelector("#fullname").value;
  let username = document.querySelector("#username").value;
  let email = document.querySelector("#email").value;
  let password = document.querySelector("#password").value;
  let confirmPassword = document.querySelector("#confirm-password").value;
  let dateOfBirth = document.querySelector("#dateOfBirth").value;
  let areFieldsValid = true;

// fullname length check
  if (fullname.length <= 0) {
    areFieldsValid = false;
    document.querySelector("#fullname_error").textContent = "*töltse ki!";
    document.querySelector("#fullname").classList.add("form-error-field");
  } else {
    document.querySelector("#fullname").classList.remove("form-error-field");
    document.querySelector("#fullname_error").textContent = "";
  }

  // username length check
  if (username.length <= 0) {
    areFieldsValid = false;
    document.querySelector("#username_error").textContent = "*töltse ki!";
    document.querySelector("#username").classList.add("form-error-field");
  } else {
    document.querySelector("#username").classList.remove("form-error-field");
    document.querySelector("#username_error").textContent = "";
  }

  // email validation
  let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email)) {
    areFieldsValid = false;
    document.querySelector("#email_error").textContent = "*érvénytelen e-mail cím!";
    document.querySelector("#email").classList.add("form-error-field");
  } else {
    document.querySelector("#email").classList.remove("form-error-field");
    document.querySelector("#email_error").textContent = "";
  }

  // password length check
  if (password.length <= 0) {
    areFieldsValid = false;
    document.querySelector("#password_error").textContent = "*töltse ki!";
    document.querySelector("#password").classList.add("form-error-field");
  } else {
    document.querySelector("#password").classList.remove("form-error-field");
    document.querySelector("#password_error").textContent = "";
  }

  // password confirmation check
  if (confirmPassword != password) {
    areFieldsValid = false;
    document.querySelector("#confirm-password_error").textContent = "*a jelszavak nem egyeznek!";
    document.querySelector("#confirm-password").classList.add("form-error-field");
  } else {
    document.querySelector("#confirm-password").classList.remove("form-error-field");
    document.querySelector("#confirm-password_error").textContent = "";
  }

  // date of birth validation
  if (!dateOfBirth) {
    areFieldsValid = false;
    document.querySelector("#dateOfBirth_error").textContent = "*töltse ki!";
    document.querySelector("#dateOfBirth").classList.add("form-error-field");
  } else {
    document.querySelector("#dateOfBirth").classList.remove("form-error-field");
    document.querySelector("#dateOfBirth_error").textContent = "";
  }

  if (areFieldsValid) {
    const data = {
      fullname: fullname,
      username: username,
      email: email,
      password: password,
      dateOfBirth: dateOfBirth
    };

    axios.post('/api/register', data)
        .then(response => {
          document.querySelector("#success").textContent = response.data + " Hamarosan át leszel irányítva!";
          document.querySelector("#error").textContent = "";
          setTimeout(function() {
          window.location.href = '/api/log';
          }, 3000);
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

const registrationForm = document.querySelector('#registration-form');
registrationForm.addEventListener('submit', registrationValidation);
