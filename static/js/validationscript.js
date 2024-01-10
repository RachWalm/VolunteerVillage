document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("submithold").addEventListener("click", function (event) {
        event.preventDefault()
        var elevenNumbers = /^\d{11}$/;
        entry = document.getElementById("id_phone").value;
        days = document.getElementById("id_time_length_days").value;
        hours = document.getElementById("id_time_length_hours").value;
        if (elevenNumbers.test(entry)) {
            if (hours <= 168) {
                if (days <= 7) {
                    alert("Days are valid!");
                    var final = document.getElementById("volunteerForm");
                    console.log(final);
                    final.submit();
                } else {
                    alert("That is more days than in a week! Please enter 7 or less.");
                }
            } else {
                alert("That is more hours per week than there is in a week! Please edit.");
            }
        } else {
            alert("Please edit your data to enter a valid phone number, which is numerical and should contain 11 digits.");
        }
    });
});