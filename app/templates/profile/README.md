# Profile Components

## `info.html`

This is used to display a user's information. Their information is passed to the template, and rendered in two sections. The
first is an image card-like structure, showing the default image, account type, and account status.

Hovering over the *Account Status* will show the status of the account in a tooltip. This is done using `Popper.js` and Bootstrap.

The second part is all the user's information. This is again done using Bootstrap's `list-group`, with custom style added via a class.

## `my-polls.html`

This displays the user's polls. As with other modules, the flow follows with an information `alert`, then a `<table>` that contains
the user's polls, and a form. 

In this case, the form is for closing a poll, i.e. changing it from *Current* to *Completed*.

A validation component exists to check if the component is actually valid, and if it is, the Submit button is activated.

Notifications will fire depending on the success of the closing of the poll.