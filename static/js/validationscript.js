// validation script for phone number, number of days and number of hours in volunteer profile
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submithold").addEventListener("click", function (event) {
        event.preventDefault() /* prevents submit*/
        var elevenNumbers = /^\d{11}$/; /*code for an eleven digit number/numerical*/
        entry = document.getElementById("id_phone").value;
        days = document.getElementById("id_time_length_days").value;
        hours = document.getElementById("id_time_length_hours").value;
        fname = document.getElementById("id_fname").value;
        lname = document.getElementById("id_lname").value;
        skilled = document.getElementById("id_skilled").value;
        if (elevenNumbers.test(entry)) {
            /*validates phone number using entry variable*/
            if (hours <= 168) {
                /*validates number of hours against 168 hours in a week*/
                if (days <= 7) {
                    /*validates number of days against 7 days in a a week*/
                    if (fname != 0) {
                        /*validates first name present*/
                        if (lname != 0) {
                            /*validates last name present*/
                            if (skilled != 0) {
                                /*validates last name present*/
                                if (days & hours >= 0) {
                                    /*validates time positive or zero*/
                                    var final = document.getElementById("volunteerForm");
                                    final.submit();
                                } else {
                                    /*alert to inform user to change time value*/
                                    alert("Time must be zero or positive.");
                                }
                            } else {
                                /*alert to inform user at least one skill required*/
                                alert("Please add at least one skill.");
                            }
                        } else {
                            /*alert to inform user last name required*/
                            alert("Please add your last name.");
                        }
                    } else {
                        /*alert to inform user first name required*/
                        alert("Please add your first name.");
                    }
                } else {
                    /*alert to inform user exceeded days in week*/
                    alert("That is more days than in a week! Please enter 7 or less.");
                }
            } else {
                /*alert to inform user exceeded hours in week*/
                alert("That is more hours per week than there is in a week! Please edit.");
            }
        } else {
            /*alert to inform user invalid phone number*/
            alert("Please edit your data to enter a valid phone number, which is numerical and should contain 11 digits.");
        }
    });
});