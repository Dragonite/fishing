let timeElements = document.getElementsByClassName('modify-time');
for (let i = 0; i < timeElements.length; i++) {
  let unformattedTime = timeElements[i].innerHTML;
  timeElements[i].innerHTML = moment.utc(unformattedTime, 'YYYY-MM-DD HH:mm:ss').local().format('DD/MM/YYYY HH:mm')
}
