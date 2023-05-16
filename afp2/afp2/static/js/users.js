var role = 3;
var uinviteLink = document.getElementById("uinvite");
var unewLink = document.getElementById("unew");
var uroleLink = document.getElementById("urole");
var upasswordLink = document.getElementById("upassword");

if (role == 2)
{
  uinviteLink.style.display = "visible";
  unewLink.style.display = "none";
  uroleLink.style.display = "none";
  upasswordLink.style.display = "none";
}
else if (role == 3)
{
    uinviteLink.style.display = "none";
    unewLink.style.display = "visible";
    uroleLink.style.display = "visible";
    upasswordLink.style.display = "visible";
}
