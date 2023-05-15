
function loginValidation() {

    let username = document.querySelector("#username").value;
    let password = document.querySelector("#password").value;
    let areFieldsValid = true;

    //username length check
    if (username.length <= 0) {
      areFieldsValid = false;
      document.querySelector("#username_error").textContent = "*töltse ki!";
      document.querySelector("#username").classList.add("form-error-field");
    }
    else {
      document.querySelector("#username").classList.remove("form-error-field");
      document.querySelector("#username_error").textContent = "";
    }
      
    //password length check
    if (password.length <= 0) {
      areFieldsValid = false;
      document.querySelector("#password_error").textContent = "*töltse ki!";
      document.querySelector("#password").classList.add("form-error-field");
    }
    else {
      document.querySelector("#password").classList.remove("form-error-field");
      document.querySelector("#password_error").textContent = "";
    }    

    if (areFieldsValid == false) return false;

    return true;
  }