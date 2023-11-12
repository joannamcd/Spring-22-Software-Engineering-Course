var currentLocation = window.location.href;

let result = currentLocation.includes("demand");

if(result == true){
    document.getElementById("link").href="https://demand.team23.sweispring22.gq/common-front-end/login.html"; 
    document.getElementById("link2").href="https://demand.team23.sweispring22.gq/demand-front-end/taasUserCreateAccount.html";
}
else if(result == false){
    document.getElementById("link").href="https://supply.team23.sweispring22.gq/common-front-end/login.html";
    document.getElementById("link2").href="https://supply.team23.sweispring22.gq/supply-front-end/fleetManagerCreateAccount.html";
}