# Index Card Components

## `card-group.html`

This is component for the cards displaying counts for polls, and users. It uses a mixture of Bootstrap cards and custom CSS.
The custom CSS takes anything inside a `rotate` class that's inside a `card-body` and rotates it, displaying a nice looking icon inside
the card representing what it is. (i.e. Users uses `fa-fw fa fa-users`). A good thing to note is that normally the icon is shown
so that it overflows the card. This is modified by using an appropriate `z-index` and also modifying the overflow property of the `card-body`.

## `card-login`

This component is the 'Welcome Message', that shows when you log in, or if you're not logged in. It detects whether the user
is a registered user or not, and then depending on that, checks the last logged in time and modifies it using `last-logged-in.js`,
a JavaScript tool that I have written.