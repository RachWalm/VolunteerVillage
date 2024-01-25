// validation script for coordinator profile first and last name
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submithold").addEventListener("click", function (event) {
        event.preventDefault() /* prevents submit*/
        fname = document.getElementById("id_fname").value;
        lname = document.getElementById("id_lname").value;
        if (fname != 0) {
            /*validates first name present*/
            if (lname != 0) {
                /* validates last name present*/
                var final = document.getElementById("volunteerForm");
                final.submit();
            } else {
                /*alert to inform user last name required*/
                alert("Please add your last name.");
            }
        } else {
            /*alert to inform user first name required*/
            alert("Please add your first name.");
        }
    });
});