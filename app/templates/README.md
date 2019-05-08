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