function ctf_flag() {
  let leet = document.querySelector('.submit-leet').value;
  let flag = document.querySelector('.submit-flag').value;

  if(leet == '' && flag == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Enter a Leet and Flag</br>Try Again</p></div>';
    return false;

  } else if(leet == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Enter a Leet Try Again</p></div>';
    return false;
    
  } else if(flag == '') {
    document.getElementById('error-submit').innerHTML = '<div class="error-submit"><p>Enter a Flag Try Again</p></div>';
    return false;
  }
}