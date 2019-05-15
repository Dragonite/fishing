let lastLoggedIn = moment(document.getElementById('last-logged-in').innerHTML).format('YYYY-MM-DD HH:mm:ss');
let now = moment().utcOffset(0).format('YYYY-MM-DD HH:mm:ss');
let timeInSeconds = moment(now).diff(moment(lastLoggedIn), 'seconds');
if (timeInSeconds < 1) {
  document.getElementById('last-logged-in-container').innerHTML = "Logged in just now."
} else if (timeInSeconds < 60) {
  document.getElementById('last-logged-in').innerHTML = moment(now).diff(moment(lastLoggedIn), 'seconds') + " seconds"
} else if (timeInSeconds >= 60 && timeInSeconds < 3600) {
  document.getElementById('last-logged-in').innerHTML = moment(now).diff(moment(lastLoggedIn), 'minutes') + " minutes"
} else if (timeInSeconds >= 3600 && timeInSeconds < 86400) {
  document.getElementById('last-logged-in').innerHTML = moment(now).diff(moment(lastLoggedIn), 'hours') + " hours"
} else {
  document.getElementById('last-logged-in').innerHTML = moment(now).diff(moment(lastLoggedIn), 'days') + " days"
}