function flag_submit() {
   let leet = document.querySelector('.leet').value;
   let flag = document.querySelector('.flag-submit').value;

   if(leet == '' && flag == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">solver is empty<h1></div>';
     return false;
     
   } else if(leet == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">leet is empty<h1></div>';
     return false;

   } else if(flag == '') {
     document.getElementById('error-submit').innerHTML = '<div class="err-submit"><h1 class="err-message">flag is empty<h1></div>';
     return false;
   }
}
function remove_succ_message() {
  document.querySelector('.success').style.display = 'none';
}
function remove_err_message() {
  document.querySelector('.error').style.display = 'none';
}
document.querySelector('.send').addEventListener('click', remove_succ_message);
document.querySelector('.send').addEventListener('click', remove_err_message);