var restartB = document.querySelector('#b');

var allitems = document.querySelectorAll('td');

function clearB() {
  for (var i = 0; i < allitems.length; i++) {
    allitems[i].textContent = '';
  }
}
function changeMark(){
  if(this.textContent === ''){
    this.textContent ='X';
  }else if (this.textContent ==='X') {
    this.textContent ='O';
  }else {
    this.textContent ='';
  }
}
restartB.addEventListener('click',clearB);

for (var i = 0; i < allitems.length; i++) {
  allitems[i].addEventListener('click',changeMark)
}
