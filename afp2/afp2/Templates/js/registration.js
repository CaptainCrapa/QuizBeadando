function registrationValidation() {
    let fullname = document.querySelector("#fullname").value;
    let username = document.querySelector("#username").value;
    let email = document.querySelector("#email").value;
    let password = document.querySelector("#password").value;
    let confirmPassword = document.querySelector("#confirm-password").value;
    let dateOfBirth = document.querySelector("#dateOfBirth").value;
    let areFieldsValid = true;
  
// fullname length check
  if (fullname.length <= 0)
  {

  }
  else
  {

  }

  // username length check
  if (username.length <= 0)
  {

  }
  else
  {

  }

  // email validation
  let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  if (!emailRegex.test(email))
  {

  }
  else
  {

  }

  // password length check
  if (password.length <= 0) 
  {

  }
  else
  {

  }

  // password confirmation check
  if (confirmPassword != password) 
  {

  }
  else
  {

  }

  // date of birth validation
  if (!dateOfBirth)
  {

  }
  else
  {

  }
}