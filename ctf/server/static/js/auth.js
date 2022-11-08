function registration_validate() {
  let user = document.querySelector('.reg-user').value;
  let pass = document.querySelector('.reg-pass').value;
  let retype_pass = document.querySelector('.reg-retype-pass').value;

  if(user == '' && pass == '' && retype_pass == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>all Field is Empty Try Again</p></div>';
    return false;

  } else if(user == '' && pass == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty</br>Try Again</p></div>';
    return false;

  } else if(user == '' && retype_pass == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty</br>Try Again</p></div>';
    return false;

  } else if(pass == '' && retype_pass == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty</br>Try Again</p></div>';
    return false;

  } else if(user == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty</br>Try Again</p></div>';
    return false;

  } else if(pass == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty</br>Try Again</p></div>';
    return false;

  } else if(retype_pass == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty</br>Try Again</p></div>';
    return false;

  } else if(pass.length < 8) {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Password Atleast 8 Digits</p></div>';
    return false;

  } else if(pass !== retype_pass) {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Password Not Matched</p></div>';
    return false;
  }
}
function login_validate() {
  let user = document.querySelector('.login-user').value;
  let pass = document.querySelector('.login-pass').value;

  if(user == '' && pass =='') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty</br>Try Again</p></div>';
    return false;

  } else if(user == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Enter a Username Try Again</p></div>';
    return false;

  } else if(pass == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Enter a Password Try Again</p></div>';
    return false;
  }
}