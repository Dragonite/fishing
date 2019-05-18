# Archive Components

## `pollArchive.html` &middot; `responseArchive.html` &middot; `userArchive.html`

Firstly, an informational area is rendered, explaining the types of polls and the requirements for archiving a poll. This is done
using Bootstrap's `alert` class, and inline styling.
 
`DataTables` is used to render a table, that lists all polls in the database. It is rendered in a `card` to keep a nice flow
for the page.

Finally, the form is provided to submit an ID to update the corresponding poll's `isActive` property.

JQuery is used to rerender the search field to a nicer, rounder search box.

Additionally, there is a Validation button that checks the field client-side to see if the ID valid for submission. More information
on this will be in `static/javascript`.

For `userArchive.html`, the date is modified using `Moment.js` so that it is no longer the server's UTC time, and reformatted
into a more readable date using JQuery.