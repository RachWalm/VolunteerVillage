const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var deleteConfirm = document.getElementById("deleteConfirm");


// Modal listening event to confirm if delete is truly required

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let id = e.target.getAttribute("coordinator_id");
        deleteConfirm.href = `delete_profile/${id}`;
        deleteModal.show();
    });
}