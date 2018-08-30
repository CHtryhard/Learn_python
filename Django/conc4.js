console.log('Connected')
// red rgb(255, 0, 0)
// yellow rgb(255, 255, 0)
// gray rgb(128, 128, 128)
var gameon = true;


while (true) {
  var p1name = prompt('Please enter the name of Player one');
  if (p1name == '' || p1name == null) {
    alert('Please enter something');
  }else {
    break;
  }
}



var turn = 1;
while (true) {
  var p2name = prompt('Please enter the name of Player Two');
  if (p2name === p1name) {
    alert('Please enter a different name');
  }else if (p2name ===''|| p2name == null) {
    alert('Please enter something');
  }else {
    break;
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
  for (var j = 0; j < 7; j++)   {
    for (var i = 5; i > 2; i--) {
      if (TG(i,j).css('background-color') !== 'rgb(128, 128, 128)' && TG(i,j).css('background-color') == TG(i-1,j).css('background-color') && TG(i,j).css('background-color') == TG(i-2,j).css('background-color') && TG(i,j).css('background-color') == TG(i-3,j).css('background-color')) {
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
  console.log(one);
  two = vertCheck();
  console.log(two);
  three = diaCheck();
  console.log(three);
  four = diaCheck2();
  console.log(three);
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
      r = BottomAva(c)
      if (r!=undefined) {
        changeColor (r,c,color);
        turn = turn + 1;
        a = wincondit()
        if (a) {
          $('h4').text('Player:' + current + ' has won!')
          gameon = false;
        }else {
          if (turn%2 === 0) {
            current = p2name
            $('h4').text(current + ': this is your turn to play.')
            color = 'rgb(255, 255, 0)'
          }else {
            current = p1name
            $('h4').text(current + ': this is your turn to play.')
            color = 'rgb(255, 0, 0)'
          }
        }
      }else{
        alert('This column is full\n Please select another column')
      }
  })
