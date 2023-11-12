	
function handleFormSubmit(event) {
    event.preventDefault();
    
    const data = new FormData(event.target);
    
    const formJSON = Object.fromEntries(data.entries());
    
    //const results = document.querySelector('.results pre');
    //results.innerText = JSON.stringify(formJSON, null, 2);
    //console.log(JSON.stringify(formJSON, null, 2));
    //const newUserData = JSON.stringify(formJSON, null, 2);
   // console.log(newUserData);
	console.log(formJSON.currentLoc + ", " + formJSON.city1 + ", " + formJSON.state1 + " " + formJSON.zip1);
	console.log(formJSON.destinationLoc + ", " + formJSON.city2 + ", " + formJSON.state2 + " " + formJSON.zip2);
	
	var start = formJSON.currentLoc + ", " + formJSON.city1 + ", " + formJSON.state1 + " " + formJSON.zip1;
	var end = formJSON.destinationLoc + ", " + formJSON.city2 + ", " + formJSON.state2 + " " + formJSON.zip2;
	
	const addresses = {"pickup_address": start, "destination_address": end}
	
	console.log(addresses);
	const sendData = JSON.stringify(addresses, null, 2);
	
  localStorage.setItem("pickup_address", start);
  localStorage.setItem("destination_address", end);
  sendOrder(sendData);
  
  }
  
  const form = document.querySelector('.order-form');
  form.addEventListener('submit', handleFormSubmit);
  


  var orderResponse = "";
  var pickup_address = "";
  var destination_address = "";
  // var destCoord = "";
  // var pickupCoord = "";
  // var timeToDest = "";
  // var timeToPickup = "";
  // var vehicleCoord = "";
  // var vehicleID = "";


  function sendOrder(newUserData) {
    const url = "https://demand.team23.sweispring22.gq/order";
    var info = newUserData;
  
    const params = {
      headers: {
        "content-type": "application/json; charset=UTF-8",
      },
      body: info,
      method: "POST",
    };
  
    fetch(url, params)
      .then((data) => {
        return data.json();
      })
      .then((result) => {
        //console.log(result);
        orderResponse = result.data;
        console.log(orderResponse);
        // test1 = result.data.destCoord;

        localStorage.setItem("destCoord", result.data.destCoord);
        localStorage.setItem("pickupCoord", result.data.pickupCoord);
        localStorage.setItem("timeToDest", result.data.timeToDest);
        localStorage.setItem("timeToPickup", result.data.timeToPickup);
        localStorage.setItem("vehicleCoord", result.data.vehicleCoord);
        localStorage.setItem("vehicleID", result.data.vehicleID);
        window.location.href = "https://demand.team23.sweispring22.gq/demand-front-end/orderConfirmation.html";

      })
      .catch((error) => console.log(error));
  
  }  



function loginCheck()
{
  if (localStorage.getItem("username") === null) {
    alert("You need to login!")
    window.location.href = "https://demand.team23.sweispring22.gq/common-front-end/login.html";
  }
}