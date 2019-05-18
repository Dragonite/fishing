$(document).ready(function () {

  $('#table-active, #table-inactive').DataTable();

  $('#table-polls, #table-responses, #table-users').DataTable( {
    "aLengthMenu": [[5, 10, 15, -1], [5, 10, 15, "All"]],
    "pageLength": 5
    } );
});