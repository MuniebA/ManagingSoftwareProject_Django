const registeredUsers = ["test@example.com", "user@example.com"]; // Add more emails as needed

function isNewUser(userEmail) {
    // Check if the provided email is in the list of registered users
    return !registeredUsers.includes(userEmail);
}

let loginForm = document.querySelector(".form");

loginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    let email = document.getElementById("email");
    let password = document.getElementById("password");

    // Check if the user is a new user
    if (isNewUser(email.value)) {
        if (validateForm(email.value, password.value)) {
            window.location.href = "test.html";
        } else {
            alert("Invalid email or password. Please try again.");
        }
    } else {
        alert("You are not a new user. Please use a different password.");
    }
});

var gErrorMsg = "";

function validateForm(userEmail, userPassword) {
    "use strict";
    var isAllOK = false;
    gErrorMsg = "";
    var emailOK = chkEmail(userEmail);
    if (emailOK && userPassword === "defaultPassword") {
        isAllOK = true;
    } else {
        gErrorMsg = "Invalid email or password. Please try again.\n";
    }
    return isAllOK;
}

function chkEmail(userEmail) {
    var result = false;
    // Corrected email pattern
    var pattern = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (pattern.test(userEmail)) {
        result = true;
    } else {
        gErrorMsg = "Enter a valid email address\n";
    }
    return result;
}

function validateInputOnBlur(inputId) {
    var objectLostFocus_id = inputId;
    var isOk = false;
    switch (objectLostFocus_id) {
        case "email":
            isOk = chkEmail(document.getElementById("email").value);
            break;
    }
    if (!isOk) {
        document.getElementById(objectLostFocus_id).style.borderColor = "red";
        document.getElementById(objectLostFocus_id).style.backgroundColor = "lightgray";
        gErrorMsg = "";
    }
}

function init() {
    // Set a default email for testing
    document.getElementById("email").value = "test@example.com";
}

window.onload = init;