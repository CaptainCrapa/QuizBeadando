var role = 3;
var qgenerateLink = document.getElementById("qgenerate");
var qdeleteLink = document.getElementById("qdelete");

if (role == 2)
{
  qgenerateLink.style.display = "visible";
  qdeleteLink.style.display = "none";
}
else if (role == 3)
{
  qdeleteLink.style.display = "visible";
  qgenerateLink.style.display = "none";
}
else
{
  qdeleteLink.style.display = "none";
  qgenerateLink.style.display = "none";
}