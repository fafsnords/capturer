let cipher = () => {
   document.querySelector('.cipher').classList.toggle('drop');
}
let stegano = () => {
   document.querySelector('.stegano').classList.toggle('drop');
}
let reverseengr = () => {
   document.querySelector('.reverseengr').classList.toggle('drop');
}
let anlysis = () => {
   document.querySelector('.analize').classList.toggle('drop');
}
let dirlisting = () => {
   document.querySelector('.dirlisting').classList.toggle('drop');
}
let recon = () => {
   document.querySelector('.recon').classList.toggle('drop');
}
document.querySelector('.crypt').addEventListener('click', cipher);
document.querySelector('.steg').addEventListener('click', stegano);
document.querySelector('.reverse').addEventListener('click', reverseengr);
document.querySelector('.analyze').addEventListener('click', anlysis);
document.querySelector('.dir').addEventListener('click', dirlisting);
document.querySelector('.rec').addEventListener('click', recon);