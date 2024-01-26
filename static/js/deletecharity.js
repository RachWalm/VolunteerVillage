/* jshint esversion: 8 */

const deleteModal = new bootstrap.Modal(document.getElementById("deleteModal"));
var deleteButtons = document.getElementsByClassName("btn-delete");
var deleteConfirm = document.getElementById("deleteConfirm");


// Modal listening event to confirm if delete is truly required

for (let button of deleteButtons) {
    button.addEventListener("click", (e) => {
        let id = e.target.getAttribute("charityid");
        deleteConfirm.href = `delete_charity/${id}`;
        deleteModal.show();
    });
}