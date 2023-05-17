var role = "adminisztrator";
var qgenerateLink = document.getElementById("qgenerate");
var qdeleteLink = document.getElementById("qdelete");

if (role == "tanar")
{
  qgenerateLink.style.display = "visible";
  qdeleteLink.style.display = "none";
}
else if (role == "adminisztrator")
{
  qdeleteLink.style.display = "visible";
  qgenerateLink.style.display = "none";
}
else
{
  qdeleteLink.style.display = "none";
  qgenerateLink.style.display = "none";
}