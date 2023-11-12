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
  
  const results = document.querySelector('.results pre');
  //results.innerText = JSON.stringify(formJSON, null, 2);
 // console.log(JSON.stringify(formJSON, null, 2));
  const newUserData = JSON.stringify(formJSON, null, 2);
  console.log(newUserData);
  sendOrder(newUserData);
  //Check this
  window.location.href = "https://demand.team23.sweispring22.gq/common-front-end/login.html";
}

const form = document.querySelector('.contact-form');
form.addEventListener('submit', handleFormSubmit);






// uncomment this on the html out of convenience
function autofillForm() {


    let form = document.forms['createAccountForm']; 

    form['firstName'].value = 'FirstName';
    form['lastName'].value = 'LastName';
    form['email'].value = 'a@a.com';
  	form['address'].value = '123 Main Street';
  	form['zip'].value = '12345';
    form['city'].value = 'Austin';
    form['password'].value = 'Hello1234!'; 
    form['confirmation'].value = 'Hello1234!';
    form['phone'].value = '1234567891';
	  form['username'].value = 'username';
	
}



function sendOrder(newUserData) {
  const url = "https://demand.team23.sweispring22.gq/taasUserRegister";
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
