//clock

function sectionTime() {
  var openHourTitle = ' Open Today '; 
  var today = new Date();
  var h = today.getHours();
  var hFinal  = h;
  var amPm = "am";
  if (h > 12) { hFinal = h - 12};
  if (h  > 11) { amPm  = "pm" };
  var m = today.getMinutes();
  var s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  if (h > 16) {openHourTitle = 'Closing Soon'} ;
  if (h < 11) {openHourTitle = 'Opening Soon'} ;
  document.getElementById('open-hours').innerHTML =
  openHourTitle; 
}
function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}
