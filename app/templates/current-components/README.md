# Archive Components

## `current-standings.html`

This uses `Chart.js` to render a current chart, based on data of each **First Past the Post** voting dataset.

Buttons for each preference are also rendered, and dynamically updated using JQuery on click. Furthermore, when each button is clicked, 
the `addData()` function for chart replaces the data for the chart for the next preference, and redraws the Chart canvas with the new selected preference.

The other information such as `Description`, `Total Votes` and such are rendered into lists.

## `vote.html`

Vote renders the form into a card for a nice flushed look. A Bootstrap `badge` keeps track of how many votes are casted in a concise manner.
Apart from the form, there are also two buttons, `Validate` and `Back`.

`Back` will redirect the user back to all current polls.

`Validate` checks that all inputs are unique, and if they are, it un-disables the Submit button, and allows submission.

Notifications are fired if a submission is successful or not. 
