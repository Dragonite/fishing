# Templates

## Main Pages

### `base.html`

`base` provides the overview of the entire application. Every page extends it, meaning that it's purpose is to house the
common components that are used on every page, at the highest level. These are `sidebar`, `header` and `imports`. These
individual components will be explained in `app/templates/components/README.md`

---

### `index.html`

`index` is the home page of the application. It includes a `card` that contains a welcome message and login information,
as well as site statistics, and a Dashboard created using `Chart.js` that shows data for 2 of the most popular polls.

---

### `current.html`

---

### `completed.html`

---

### `create.html`

`create` is the form used to create a poll. It is created using Flask's `WTForms`. The key things to note in this form
is the integration the entire form has with Bootstrap 4, and the different JavaScript functions that are included. 

Each different input has the class `form-control` attached, giving the field the curved sleek look, and consistent sizing.
The Title and Description have custom JavaScript written that tracks the amount of characters used in the boxes. This will
be elaborated in `app/static/javascript/README.md` .

Create Choices uses Bootstrap's input groups to create nice input fields with buttons, and dynamically adds and removes fields
depending on the buttons clicked. Again, elaboration will be in `app/static/javascript/README.md`.

Browser `localStorage` is also implemented. If a user clicks off the page, or refreshes, field values will be saved and
added back to preserve the last position of the form. This was chosen over constantly resubmitting to reduce the amount of requests
needed. On `Save`, the form will save its contents. On `Clear`, all fields will be reset. On `Submit`, the regular submit function
will be run.

---

### `profile.html`

`profile` is broken into two parts, *My Info* and *Statistics*. `profile` is a page that gives an overview of the current user. 
The fields are rendered as inputs, and the `Update` button allows a `Post` request to fire to update the user. `Statistics` uses
`Chart.js` to render linkable charts that link to the user's total amount of polls, their open and closed polls. The individual
tabs are further elaborated in the `profile` directory.

---

### `users`

`users` is a page that provides an overview of all the users in the system. They are split into two tabs, `Active` and 
`Inactive`. As user accounts are never fully deleted, marking them as `false` for `isActive` will disable the account, but
still keep their information in the system, so that it shows on their votes and polls.

---

### `help`

`help` provides information on the website in 3 tabs: `About`, `Algorithm` and `Acknowledgements`. 

`About` explains the functionality of the website and how polls and votes are made.

`Algorithm` explains the algorithm behind the calculation of the winner.

`Acknowledgements` explains the Libraries and Tutorials used, as well as acknowledging contributions by individuals.

---

## Directories

All elaborations for the following files inside the directories below will be included in individual `README.md`'s in each directory.

### `auth`

A directory for authorization modules.

Contains:
- `login.html`

---

### `components`

A directory for base components.

Contains: 
- `header.html`
- `imports.html`
- `sidebar.html`

---

### `errors`

A directory for errors in the application.

Contains:
- `404.html`
- `500.html`

---

### `help`

A directory that contains the tabs in the `help.html` page.

Contains:
- `about.html`
- `acknowledgements.html`
- `algorithm.html`

---

### `index`

A directory for `index.html`'s widgets.

Contains:
- `card-group.html`
- `card-login.html`

---

### `profile`

A directory that contains the tabs in the `profile.html` page.

Contains:
- `info.html`
- `statistics.html`