/* jshint esversion: 8 */

/* validation script for volunteer profile form phone number, 
 * number of days and number of hours 
 * and if all the needed boxes are filled out in volunteer profile
 */
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submithold").addEventListener("click", function (event) {
        event.preventDefault() /* prevents submit*/
        if (phone()) {
            if (time()) {
                if (person()) {
                    if (skill()) {
                        var final = document.getElementById("volunteerForm");
                        final.submit();
                    }
                }
            }
        }
    });
});

function time() {
    let days = document.getElementById("id_time_length_days").value;
    let hours = document.getElementById("id_time_length_hours").value;
    if (hours <= 168) {
        /*validates number of hours against 168 hours in a week*/
        if (days <= 7) {
            /*validates number of days against 7 days in a a week*/
            if (positive()) {
                /*validates time positive or zero*/
                return true;
            }
        } else {
            /*alert to inform user exceeded days in week*/
            alert("That is more days than in a week! Please enter 7 or less.");
        }
    } else {
        /*alert to inform user exceeded hours in week*/
        alert("That is more hours per week than there is in a week! Please edit.");
    }
}

function positive() {
    let days = document.getElementById("id_time_length_days").value;
    let hours = document.getElementById("id_time_length_hours").value;
    if (days >= 0) {
        if (hours >= 0) {
            /*validates time positive or zero*/
            return true;
        } else {
            /*alert to inform user to change time value*/
            alert("Time must be zero or positive.");
        }
    } else {
        /*alert to inform user to change time value*/
        alert("Time must be zero or positive.");
    }
}

function person() {
    var fname = document.getElementById("id_fname").value;
    var lname = document.getElementById("id_lname").value;
    if (fname != 0) {
        /*validates first name present*/
        if (lname != 0) {
            /*validates last name present*/
            return true;
        } else {
            /*alert to inform user last name required*/
            alert("Please add your last name.");
        }
    } else {
        /*alert to inform user first name required*/
        alert("Please add your first name.");
    }
}

function phone() {
    var elevenNumbers = /^\d{11}$/; /*code for an eleven digit number/numerical*/
    var entry = document.getElementById("id_phone").value;
    if (elevenNumbers.test(entry)) {
        /*validates phone number using entry variable*/
        return true;
    } else {
        /*alert to inform user invalid phone number*/
        alert("Please edit your data to enter a valid phone number, which is numerical and should contain 11 digits.");
    }
}

function skill() {
    var skilled = document.getElementById("id_skilled").value;
    if (skilled != 0) {
        /*validates whether any skills have been chosen*/
        return true;
    } else {
        /*alert to inform user at least one skill required*/
        alert("Please add at least one skill.");
    }
}