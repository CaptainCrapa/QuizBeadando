var role = 3;
var roleLink = document.getElementById("role");

if (role == 1)
{
  roleLink.textContent = "Diák"
}
else if (role == 3)
{
  roleLink.textContent = "Adminisztátor"
}
else if (role == 2)
{
  roleLink.textContent = "Tanár";
}