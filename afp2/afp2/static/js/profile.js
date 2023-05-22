function togglePasswordVisibility() {
  var password = document.getElementById("password");
  var toggle = document.getElementById("toggle");

  if (toggle.checked) {
    password.style.display = "inline";
  } else {
    password.style.display = "none";
  }
}