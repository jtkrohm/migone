
//clock

function startTime() {
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
  document.getElementById('clock').innerHTML =
  hFinal + ":" + m + ":" + s + " " + amPm; 
  var t = setTimeout(startTime, 500);
}
function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}

