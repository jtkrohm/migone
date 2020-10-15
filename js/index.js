//core js file
//modular js file
//page specific js file ##

const clockTag = document.getElementById('clock');
const openHourTag = document.getElementById('open-hours');
var openHourTitle = ' Open Today '; 

function sectionTime() {
  let today = new Date();
  let h = today.getHours();
  let hFinal  = h;
  let amPm = "am";
  if (h > 16) {openHourTitle = 'Closing Soon'} ;
  if (h < 10) {openHourTitle = 'Opening Soon'} ;
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  openHourTag.innerHTML = openHourTitle; 
}

function checkTime(i) {
  if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
  return i;
}
//clock

function startTime() {
  let today = new Date();
  let h = today.getHours();
  let hFinal  = h;
  let amPm = "am";
  if (h > 12) { hFinal = h - 12};
  if (h  > 11) { amPm  = "pm" };
  let m = today.getMinutes();
  let s = today.getSeconds();
  m = checkTime(m);
  s = checkTime(s);
  document.getElementById('clock').innerHTML =
  hFinal + ":" + m + ":" + s + " " + amPm; 
  let t = setTimeout(startTime, 500);
}
