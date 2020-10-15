//core js file
//modular js file
//page specific js file ##
  const clockTag = document.getElementById('clock');
  const openHourTag = document.getElementById('open-hours');
  const openHourTitle = ' Open Today '; 
  let today = new Date();
  let h = today.getHours();
  let hFinal  = h;
  const amPm = "am";
  let m = today.getMinutes();
  let s = today.getSeconds();
  let m = checkTime(m);
  let s = checkTime(s);

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
