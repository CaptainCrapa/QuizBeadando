var role = 'diak';
var roleLink = document.getElementById("role");

if (role == 'diak')
{
  roleLink.textContent = "Diák"
}
else if (role == 'adminisztrator')
{
  roleLink.textContent = "Adminisztátor"
}
else if (role == 'tanar')
{
  roleLink.textContent = "Tanár";
}