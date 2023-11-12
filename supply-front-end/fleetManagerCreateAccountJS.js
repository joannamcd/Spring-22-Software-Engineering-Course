function validateForm() 
{
	//validatePassword()
    let form = document.forms['createAccountForm'];

 
    if (form['password'].value != form['confirmation'].value) 
	{
        console.log("Passwords dont match");
		alert("The passwords dont match")
		document.getElementById("pword").reset();
		document.getElementById("pword2").reset();
		

    }

    //return false;

}




var confirmPassword = document.forms['createAccountForm']['confirmation'];

var Pword = document.forms['createAccountForm']['password'];


function validatePassword(){
  if(Pword.value != confirmPassword.value) {
    confirmPassword.setCustomValidity("Passwords Don't Match***************");
  } else {
    confirmPassword.setCustomValidity('');
  }
}

Pword.onchange = validatePassword;
confirmPassword.onkeyup = validatePassword;






	
function handleFormSubmit(event) {
  event.preventDefault();
  
  const data = new FormData(event.target);
  
  const formJSON = Object.fromEntries(data.entries());
  //results.innerText = JSON.stringify(formJSON, null, 2);
 // console.log(JSON.stringify(formJSON, null, 2));
  const newUserData = JSON.stringify(formJSON, null, 2);
  console.log(newUserData);
  sendOrder(newUserData);
}

const form = document.querySelector('.account-form');
form.addEventListener('submit', handleFormSubmit);





function sendOrder(newUserData) {
  const url = "https://supply.team23.sweispring22.gq/fleetManagerRegister";
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
      console.log(result);
    })
    .catch((error) => console.log(error));

}
