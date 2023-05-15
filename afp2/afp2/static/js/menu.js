var role = "tanar";
var usersLink = document.getElementById("users");

if (role == 'tanar' || role == 'adminisztrator')
{
  usersLink.style.display = "visible";
}
else
{
  usersLink.style.display = "none";
}