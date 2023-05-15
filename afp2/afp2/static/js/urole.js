function rolesetValidation() {
    let username = document.querySelector("#username").value;
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

  if (areFieldsValid == false) return false;

  return true;
}