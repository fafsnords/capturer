function register() {
   let username = document.querySelector('.username').value;
   let password = document.querySelector('.password').value;
   let retype_password = document.querySelector('.retype-password').value;

   if(username == '' && password == '' && retype_password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">empty try again<h1></div>';
     return false;

   } else if(username == '' && password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">username and password is empty<h1></div>';
     return false;

   } else if(username == '' && retype_password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">username and retype password is empty<h1></div>';
     return false;

   } else if(password == '' && retype_password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">password must retype<h1></div>';
     return false;

   } else if(username == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">username is empty<h1></div>';
     return false;

   } else if(password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">password is empty<h1></div>';
     return false;

   } else if(retype_password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">retype the password<h1></div>';
     return false;

   } else if(password.length < 8) {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">password atleast 8 digit<h1></div>';
     return false;

   } else if(password !== retype_password) {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">password not matched<h1></div>';
     return false;
   }
}
function login() {
   let username = document.querySelector('.username').value;
   let password = document.querySelector('.password').value;
   
   if(username == '' && password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">Enter username and password<h1></div>';
     return false;

   } else if(username == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">Enter username<h1></div>';
     return false;

   } else if(password == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">Enter password<h1></div>';
     return false;
   }
}
function remove_register_error() {
    document.querySelector('.error-register').style.display = 'none';
}
function remove_login_error() {
    document.querySelector('.error-login').style.display = 'none';
}