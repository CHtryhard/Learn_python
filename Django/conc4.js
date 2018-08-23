console.log('Connected')
// var p1name = prompt('Please enter the name of Player one')
// while (true) {
//   var p2name = prompt('Please enter the name of Player Two')
//   if (p2name === p1name) {
//     alert('Please enter a different name')
//   }else {
//     break
//   }
//
// }
//
// $('#changeTxT').text(p1name + ": it is your turn to play")
$('td').click(function(event){
  console.log($(this).closest("td").index());
  console.log($(this).closest("tr").index());
})
