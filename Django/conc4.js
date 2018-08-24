console.log('Connected')
// red rgb(255, 0, 0)
// yellow rgb(255, 255, 0)
// gray rgb(128, 128, 128)
var gameon = true;
var p1name = prompt('Please enter the name of Player one')
var turn = 1;
while (true) {
  var p2name = prompt('Please enter the name of Player Two')
  if (p2name === p1name) {
    alert('Please enter a different name')
  }else {
    break
  }
}

var table = $('#matrix');
// function checkWin () {
//   // horizontal check
//
// }

function TG(r,c) {
  return table.find('tr').eq(r).find('td').eq(c).find('button')
}
function horiCheck (){
  for (var i = 5; i > -1; i--) {
    for (var j = 0; j < 4; j++) {
      if (TG(i,j).css('background-color') !== 'rgb(128, 128, 128)' && TG(i,j).css('background-color') == TG(i,j+1).css('background-color') && TG(i,j).css('background-color') == TG(i,j+2).css('background-color') && TG(i,j).css('background-color') == TG(i,j+3).css('background-color')) {
        return true;
      }
      }
  }
}

function vertCheck (){
  for (var i = 0; i < 7; i++) {
    for (var j = 5; j > 2; j--) {
      if (TG(i,j).css('background-color') !== 'rgb(128, 128, 128)' && TG(j,i).css('background-color') == TG(j-1,i).css('background-color') && TG(j,i).css('background-color') == TG(j-2,i).css('background-color') && TG(j,i).css('background-color') == TG(j-3,i).css('background-color')) {
        return true;
      }
      }
  }
}

function diaCheck (){
  for (var i = 5; i > 2; i--) {
    for (var j = 0; j < 4; j++) {
      if (TG(i,j).css('background-color') !== 'rgb(128, 128, 128)' && TG(i,j).css('background-color') == TG(i-1,j+1).css('background-color') && TG(i,j).css('background-color') == TG(i-2,j+2).css('background-color') && TG(i,j).css('background-color') == TG(i-3,j+3).css('background-color')) {
        return true;
      }
      }
  }
}
function diaCheck2 (){
  for (var i = 5; i > 2; i--) {
    for (var j = 6; j >2; j--) {
      if (TG(i,j).css('background-color') !== 'rgb(128, 128, 128)' && TG(i,j).css('background-color') == TG(i-1,j-1).css('background-color') && TG(i,j).css('background-color') == TG(i-2,j-2).css('background-color') && TG(i,j).css('background-color') == TG(i-3,j-3).css('background-color')) {
        return true;
      }
      }
  }
}
function wincondit (){
  one = horiCheck();
  two = vertCheck();
  three = diaCheck();
  four = diaCheck2();
  if (one||two||three||four) {
    return true;
  }

}

function changeColor (r,c,color){
  return TG(r,c).css('background-color',color);
}
function BottomAva(c){
  for (var i = 5; i > -1; i--) {
    if (TG(i,c).css('background-color') === 'rgb(128, 128, 128)') {
      return i;
    }
  }
}
var current = p1name
$('h4').text(p1name + ': this is your turn to play.')
var color = 'rgb(255, 0, 0)'

table.find('button').on('click',function () {
    var c = $(this).closest("td").index();
    var r = $(this).closest("tr").index();
    console.log('the row is ',r)
    console.log('the column is ',c)
    r = BottomAva(c)
    console.log('avaliable r ',r)
    if (r!=undefined) {
      changeColor (r,c,color);
      turn = turn + 1;
      if (turn%2 === 0) {
        current = p2name
        $('h4').text(current + ': this is your turn to play.')
        color = 'rgb(255, 255, 0)'
      }else {
        current = p1name
        $('h4').text(current + ': this is your turn to play.')
        color = 'rgb(255, 0, 0)'
      }
      a = wincondit()
      if (a) {
        alert('Player:' + current + ' has won!')
      }

    }else{
      alert('This column is full\n Please select another column')
    }
})
