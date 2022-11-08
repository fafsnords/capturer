let cryptography = () => {
   document.querySelector('.cipher-results').classList.toggle('drop');
}
let steganography = () => {
   document.querySelector('.stegano-results').classList.toggle('drop');
}
let reverse_engineering = () => {
   document.querySelector('.reverse-engineering-results').classList.toggle('drop');
}
let analysis = () => {
   document.querySelector('.analysis-results').classList.toggle('drop');
}
let directory_listing = () => {
   document.querySelector('.directory-listing-results').classList.toggle('drop');
}
let reconnaissance = () => {
   document.querySelector('.reconnaissance-results').classList.toggle('drop');
}
document.querySelector('.cryptography').addEventListener('click', cryptography);
document.querySelector('.steganography').addEventListener('click', steganography);
document.querySelector('.reverse-engineering').addEventListener('click', reverse_engineering);
document.querySelector('.analysis').addEventListener('click', analysis);
document.querySelector('.directory-listing').addEventListener('click', directory_listing);
document.querySelector('.reconnaissance').addEventListener('click', reconnaissance);