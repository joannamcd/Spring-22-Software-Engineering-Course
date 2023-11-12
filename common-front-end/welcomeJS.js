
var localName;
localName = localStorage.getItem("username");
document.getElementById("name").innerHTML = localName;


function loginCheck()
{
  if (localStorage.getItem("username") === null) {
    alert("You need to login!")
    window.location.href = "https://demand.team23.sweispring22.gq/common-front-end/login.html";
}

}