var currentLocation = window.location.href;
// result == true means demand
let myResult = currentLocation.includes("demand");

if(myResult == true){
  document.getElementById("title").innerHTML = "User Log in!"; 
  document.getElementById("link1").href="https://demand.team23.sweispring22.gq/homepage.html";
  document.getElementById("link2").href="https://demand.team23.sweispring22.gq/demand-front-end/taasUserCreateAccount.html";
  document.getElementById("link3").href="https://demand.team23.sweispring22.gq/common-front-end/login.html";
}
else if(myResult == false){
  document.getElementById("title").innerHTML = "Fleet Manager Log in!"; 
  document.getElementById("link1").href="https://supply.team23.sweispring22.gq/homepage.html";
  document.getElementById("link2").href="https://supply.team23.sweispring22.gq/supply-front-end/fleetManagerCreateAccount.html";
  document.getElementById("link3").href="https://supply.team23.sweispring22.gq/common-front-end/login.html";

}

function sendForm() 
{

    let form = document.forms['logInForm'];


	console.log("Here are the values from the form:")

    console.log(form['username'].value);
    console.log(form['password'].value);
	
	//return false;

}

// for debugging purposes

function autofillForm() 
{
    let form = document.forms['logInForm']; 
	form['username'].value = 'username';
    form['password'].value = 'Hello1234!';

}

function myVisibilityFunction() {
    var x = document.getElementById("pwd");
    if (x.type === "password") {
      x.type = "text";
    } else {
      x.type = "password";
    }
  }


	
function handleFormSubmit(event) {
    event.preventDefault();
    
    const data = new FormData(event.target);
    //console.log(data.entries());
    
    const formJSON = Object.fromEntries(data.entries());
    console.log(formJSON);

    if(myResult == true){
      formJSON.side = "demand";
    }
    else if(myResult == false)
    {
      formJSON.side = "supply";
    }
    console.log(formJSON);
    const newUserData = JSON.stringify(formJSON, null, 2);

    // if(myResult == true){
    // newUserData.side = "demand";
    // }
    // else if(myResult == false){
    //   newUserData.side = "supply";
    // }
    console.log(newUserData);
    localStorage.setItem("username", formJSON.username);
    sendOrder(newUserData);

  }
  
  const form = document.querySelector('.login-form');
  form.addEventListener('submit', handleFormSubmit);
  

  // function handleFormSubmit2(event) {
  //   event.preventDefault();
    
  //   const data = new FormData(event.target);
    
  //   const formJSON = Object.fromEntries(data.entries());
  //   localStorage.setItem("username", formJSON.username);
  // }

  var loginResponse = "";

  function sendOrder(newUserData) {
    let url = "";
    if(myResult == true)
    {
     url = "https://demand.team23.sweispring22.gq/login";
    }
    else
    {
     url = "https://supply.team23.sweispring22.gq/login";
    }
    
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
        loginResponse = result.data;
        console.log(loginResponse);
        // below here should work...
        if(loginResponse === "goodLogin")
        {
          if(myResult == true)
          {
          window.location.href = "https://demand.team23.sweispring22.gq/welcome.html";
          }
          else if(myResult == false)
          {
            window.location.href = "https://supply.team23.sweispring22.gq/supply-front-end/fleetManagerDashboard.html";
          }
        }
        else if(loginResponse === "badLogin")
        {
          alert("Login Failed... Incorrect Username or Password... Please Try Again!")
        }
      })
      .catch((error) => console.log(error));
  
  }  