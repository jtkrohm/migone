//core js file
//modular js file
//page specific js file ##

const clockTag = document.getElementById('clock');
const openHourTag = document.getElementById('open-hours');
var openHourTitle = ' Open Today '; 

function sectionTime() {
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
    clockTag.innerHTML =
    hFinal + ":" + m + ":" + s + " " + amPm; 
    var t = setTimeout(sectionTime, 500);

    var today = new Date();
    var h = today.getHours();
    var hFinal  = h;
    var amPm = "am";
    if (h > 16) {openHourTitle = 'Closing Soon'} ;
    if (h < 10) {openHourTitle = 'Opening Soon'} ;
    var m = today.getMinutes();
    var s = today.getSeconds();
    m = checkTime(m);
    s = checkTime(s);
    openHourTag.innerHTML = openHourTitle; 
}

function checkTime(i) {
    if (i < 10) {i = "0" + i};  // add zero in front of numbers < 10
    return i;
}

document.addEventListener('DOMContentLoaded', sectionTime );





