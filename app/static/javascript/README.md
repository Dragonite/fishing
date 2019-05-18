# JavaScript Functions

## `create_form_storage.js`

This uses `localStorage()` to temporarily store variables for the *Title* and *Description* fields of the Create Poll form.

It uses Document Object Model to target certain components.

Two functions are provided:

`handleSave()` - Saves the Title and Description

`handleClear()` - Clears `localStorage()` only for Create Poll.

## `format-time.js`

This uses `Moment.js` and takes the time rendered on the page (by default it is in UTC), and turns it into a `moment`, and 
converts it to the equivalent local time that is browser dependent. 

It then formats the time into a more readable format commonly used in Australia, `DD/MM/YYYY HH:mm`.

## `function.js`

This is the character-counter element, `countCharacters(maxCharacters, source, target)`.

`maxCharacters` - The maximum amount of characters the targeted element can have.

`source` - The field that needs the count kept of.

`target` - The DOM element that you want to hold your dynamic count.

## `jq.js`

JQuery for `DataTables`. Initializing certain `<table>` tags to use the `DataTables` library, and also customizing certain tables
such as polls, as there are not enough for the default 10 per page.

## `last-logged-in.js`

Takes the default last logged in time, in UTC and a bad format, converts it into a `moment` using `Moment.js` and calculates the difference
with the local time in UTC. The result is then parsed depending on the length, allowing displays such as:

- Last Logged in Just Now
- Last Logged in 10 seconds ago
- Last Logged in 10 minutes ago
- Last Logged in 10 hours ago
- Last Logged in 10 days ago

## `notify.js`

Notification library that takes Bootstrap 4's notifications and makes them into dynamic notifications.

## `ordinal.js`

As we hard code 10 options, the ordinals of cardinals can only go from:

*Zeroth, First, Second ... Tenth*. 

This function takes a *cardinal* between 0 and 10 inclusive, and returns its *ordinal*.

## `tabs.js`

JavaScript for displaying tabs, and rendering them to be active or not.