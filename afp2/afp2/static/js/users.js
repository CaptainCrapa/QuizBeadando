var role = 'adminisztrator';
var uinviteLink = document.getElementById("uinvite");
var unewLink = document.getElementById("unew");
var uroleLink = document.getElementById("urole");
var upasswordLink = document.getElementById("upassword");

if (role == 'tanar')
{
  uinviteLink.style.display = "visible";
  unewLink.style.display = "none";
  uroleLink.style.display = "none";
  upasswordLink.style.display = "none";
}
else if (role == 'adminisztrator')
{
    uinviteLink.style.display = "none";
    unewLink.style.display = "visible";
    uroleLink.style.display = "visible";
    upasswordLink.style.display = "visible";
}
