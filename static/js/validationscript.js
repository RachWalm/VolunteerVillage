// validation script for phone number, number of days and number of hours in volunteer profile
document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submithold").addEventListener("click", function (event) {
        event.preventDefault() /* prevents submit*/
        var elevenNumbers = /^\d{11}$/; /*code for an eleven digit number/numberical*/
        entry = document.getElementById("id_phone").value;
        days = document.getElementById("id_time_length_days").value;
        hours = document.getElementById("id_time_length_hours").value;
        if (elevenNumbers.test(entry)) {
            /*validates phone number using entry variable*/
            if (hours <= 168) {
                /*validates number of hours against 168 hours in a week*/
                if (days <= 7) {
                    /*validates number of days against 7 days in a a week*/
                    var final = document.getElementById("volunteerForm");
                    final.submit();
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