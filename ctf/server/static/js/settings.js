function username_validate() {
   let new_user = document.querySelector('.new-user').value;
   let current_user = document.querySelector('.current-user').value;
   let pass = document.querySelector('.pass').value;

   if(new_user == '' && current_user == '' && pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>all Field is Empty Try Again</p></div>';
     return false;

   } else if(new_user == '' && current_user == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty Try Again</p></div>';
     return false;

   } else if(new_user == '' && pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty Try Again</p></div>';
     return false;

   } else if(current_user == '' && pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty Try Again</p></div>';
     return false;

   } else if(new_user == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;

   } else if(current_user == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;

   } else if(pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;
   }
}
function password_validate() {
   let user = document.querySelector('.user').value;
   let new_pass = document.querySelector('.new-pass').value;
   let current_pass = document.querySelector('.current-pass').value;

   if(user == '' && new_pass == '' && current_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>all Field is Empty Try Again</p></div>';
     return false;

   } else if(user == '' && new_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty Try Again</p></div>';
     return false;

   } else if(user == '' && current_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty Try Again</p></div>';
     return false;

   } else if(new_pass == '' && current_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The Two Field is Empty Try Again</p></div>';
     return false;

   } else if(user == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;

   } else if(new_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;

   } else if(current_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;
     
   } else if(new_pass.length < 8) {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Password Atleast 8 Digits</p></div>';
    return false;
  }
}
function delete_user_validate() {
   let del_user = document.querySelector('.del-user').value;
   let del_pass = document.querySelector('.del-pass').value;

   if(del_user == '' && del_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>all Field is Empty Try Again</p></div>';
     return false;

   } else if(del_user == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;

   } else if(del_pass == '') {
     document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>The One Field is Empty Try Again</p></div>';
     return false;
   }
}
let change_username = () => {
    document.querySelector('.change-username-form').classList.toggle('drop');
}
let change_password = () => {
    document.querySelector('.change-password-form').classList.toggle('drop');
}
let delete_account = () => {
    document.querySelector('.delete-account-form').classList.toggle('drop');
}
document.querySelector('.change-username').addEventListener('click', change_username);
document.querySelector('.change-password').addEventListener('click', change_password);
document.querySelector('.delete-account').addEventListener('click', delete_account);