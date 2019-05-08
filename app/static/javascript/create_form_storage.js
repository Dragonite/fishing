let testObject = localStorage.createForm ? localStorage.createForm : JSON.stringify({title: "", description: "", choices: []});
    localStorage.setItem('createForm', testObject);
    $(document).ready(function () {
      $('#title').val(JSON.parse(localStorage.createForm).title);
      $('#description').val(JSON.parse(localStorage.createForm).description);
    });
    document.getElementById('save-button').addEventListener('click', handleSave);
    document.getElementById('clear-button').addEventListener('click', handleClear);

    function handleSave() {
      let createFormAttributes = JSON.parse(localStorage.createForm);
      createFormAttributes.title = document.getElementById('title').value;
      createFormAttributes.description = document.getElementById('description').value;
      localStorage.setItem('createForm', JSON.stringify(createFormAttributes));
      Notify("Your current fields have been saved.", null, null, 'success');
    }

    function handleClear() {
      localStorage.setItem('createForm', JSON.stringify({title: "", description: "", choices: []}));
      location.reload();
      Notify("Your fields have been reset.", null, null, 'success');
    }