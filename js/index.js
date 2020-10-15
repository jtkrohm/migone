//core js file
//modular js file
//page specific js file ##

  const clockTag = document.getElementById('clock');
  const openHourTag = document.getElementById('open-hours');
  var openHourTitle = ' Open Today '; 
  var today = new Date();
  var h = today.getHours();
  var hFinal  = h;
  var amPm = "am";
  var m = today.getMinutes();
  var s = today.getSeconds();
  var m = checkTime(m);
  var s = checkTime(s);

function sectionTime() {
  if (h > 12) { hFinal = h - 12};
  if (h  > 11) { amPm  = "pm" };
  if (h > 16) {openHourTitle = 'Closing Soon'} ;
  if (h < 10) {openHourTitle = 'Opening Soon'} ;
  openHourTag.innerHTML = openHourTitle; 
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}
//clock

function startTime() {
  if (h > 12) { hFinal = h - 12};
  if (h  > 11) { amPm  = "pm" };
  m = checkTime(m);
  s = checkTime(s);
  clockTag.innerHTML =  hFinal + ":" + m + ":" + s + " " + amPm; 
  var t = setTimeout(startTime, 500);
}
