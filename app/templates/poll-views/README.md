# Poll Views

Poll Views represent what happens after you click on `Vote` for *Current*, or `View Results` for *Completed*.

## `currentPollView.html`

For current poll view, the first thing that happens is a check for Archive status is fired, so that if the poll is archived,
an alert is shown indicating that the poll is deleted, and cannot be viewed.

Two tabs are rendered. The first is *Vote*, explained in `current-components/vote.html`, and the second is *Current Standings*, 
explained in `current-components/current-standings.html`.

## `completedPollView.html`

For completed, the same Archive status is checked. Then using `Chart.js`, a chart is rendered showing a total of each preference's votes.
Above the chart, the winner's name is rendered, then a list of information regarding the poll is rendered.