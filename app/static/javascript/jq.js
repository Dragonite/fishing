// onclick="$('.elem-demo').notify('Hello Box');"

// $(document).ready(function () {
//   $("p").click(function (event) {
//     alert("The link will no longer take you to jquery.com");
//     event.preventDefault();
//   });

//   $('.elem-demo').notify(
//     "Test", 
//     { position: 'right middle' }
//   );
//   // $('.elem-demo').click(function () {
//   //   // alert('Button Clicked');

//   // });
// });

$(document).ready(function () {
  $(".test").click(function () {
    Notify("This is a test message.");
  });

  $("#Hi").click(function () {
    // Notify("Submission Attempt")
    Notify("Form Submission");
    // alert("Form Submission");
  });

  $('#table-active, #table-inactive').DataTable();

  $('#table-polls, #table-responses, #table-users').DataTable( {
    "aLengthMenu": [[5, 10, 15, -1], [5, 10, 15, "All"]],
    "pageLength": 5
    } );
});