# Components

## `header.html`

The header takes the title and dynamically renders it depending on the page that it is on.

If a user is anonymous, the Register Account button appears, and links to `register.html`. Otherwise, it renders
*Logged In As FirstName LastName*. As *LastName* is not optional, it renders dependant on what the user object passed is.

The title and 'Logged In As' are contained using Flexbox, so that when the screen is shrunk, the 'Logged In As' component doesn't snap underneath the title.

## `imports.html` 

Self explanatory, all imports and libraries are outlined in `README.md` at the base directory.

## `sidebar.html`

Uses nav elements and creates a fixed sidebar that stays there regardless of the scrolling of the body element.

Each element has an assigned `Font Awesome` icon that is of fixed width, so that it's clear what each element means.

The logo is also a `Font Awesome` fish icon, just a larger size.