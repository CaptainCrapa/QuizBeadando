
function loginValidation(event) {
  event.preventDefault();

  let username = document.querySelector("#username").value;
  let password = document.querySelector("#password").value;
  let areFieldsValid = true;
  let sentence;
  let words;
  let name;

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

  if (areFieldsValid) {
    const data = {
      username: username,
      password: password,
    };

    axios.post('/api/login', data)
        .then(response => {
          console.log(response.data);
          sentence = response.data;
          words = sentence.split(" ");
          name = words[2];
          document.querySelector("#success").textContent = response.data + " Át leszel irányítva!";
          document.querySelector("#error").textContent = "";
          setTimeout(function() {
          window.location.href = '/api/menu';
          }, 1500);
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

    if (name != null){
          axios.post('/api/glbl', name)
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error);
          document.querySelector('#error').textContent = "Hiba. További információ a konzolban!";
        });
    }
  }
}

const loginForm = document.querySelector('#login-form');
loginForm.addEventListener('submit', loginValidation);