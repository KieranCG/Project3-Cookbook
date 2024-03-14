document.addEventListener("DOMContentLoaded", function() {
    // sidenav initialization
    let sidenav = document.querySelectorAll(".sidenav");
    M.Sidenav.init(sidenav);

    // select initialization
    let selects = document.querySelectorAll("select");
    M.FormSelect.init(selects);

    // collapsible initializataion
    let collapsibles = document.querySelectorAll(".collapsible");
    M.Collapsible.init(collapsibles);

    // Initialize the delete modal
    let deleteModal = document.getElementById('deleteModal');
    let deleteModalInstance = M.Modal.init(deleteModal);

    // Handle delete button clicks
    let deleteButtons = document.querySelectorAll('.delete-btn');

    deleteButtons.forEach(function(button) {
        button.addEventListener('click', function(event) {
            event.preventDefault();
            var recipeId = this.getAttribute('data-recipe-id');
            var deleteUrl = "/delete_recipe/" + recipeId; // Construct the delete URL
            var deleteButton = document.getElementById('deleteButton');
            deleteButton.setAttribute('href', deleteUrl);
            deleteModalInstance.open();
        });
    });
});