<<<<<<< HEAD:main/Scripts/cateringSystem/scripts/HorngEn_scripts.js
// Get references to the delivery and shipping address input fields
const deliveryAddressInput = document.getElementById('address');
const deliveryCityInput = document.getElementById('city');
const deliveryPostalCodeInput = document.getElementById('postal-code');

const shippingAddressInput = document.getElementById('ship-address');
const shippingCityInput = document.getElementById('ship-city');
const shippingPostalCodeInput = document.getElementById('ship-postal-code');

// Add an event listener to the delivery options
document.querySelectorAll('input[name="delivery-option"]').forEach((option) => {
    option.addEventListener('change', () => {
        // Check if a delivery option is selected
        if (option.checked) {
            // Copy delivery address to shipping address fields
            shippingAddressInput.value = deliveryAddressInput.value;
            shippingCityInput.value = deliveryCityInput.value;
            shippingPostalCodeInput.value = deliveryPostalCodeInput.value;
        }
    });
});

// Get references to the payment method and QR code image elements
const paymentMethodInput = document.getElementById('ewallet');
const qrCodeImage = document.getElementById('qr-code');
const cardDetailsForm = document.querySelector('.card-details-form');

// Add an event listener to the payment method input
paymentMethodInput.addEventListener('change', () => {
    // Check if the "E-Wallet" option is selected
    if (paymentMethodInput.checked) {
        // Show the QR code image
        qrCodeImage.style.display = 'block';
        // Hide the card details form
        cardDetailsForm.style.display = 'none';
    } else {
        // Hide the QR code image if another option is selected
        qrCodeImage.style.display = 'none';
    }
});

// Get reference to the "Cards" and "Cash" options
const cardOption = document.getElementById('cards');
const cashOption = document.getElementById('cash');

// Add event listeners to the payment options
cardOption.addEventListener('change', () => {
    // Check if the "Cards" option is selected
    if (cardOption.checked) {
        // Show the card options and card details form
        cardDetailsForm.style.display = 'block';
    } else {
        // Hide the card options and card details form if another option is selected
        cardDetailsForm.style.display = 'none';
    }
});

cashOption.addEventListener('change', () => {
    // Check if the "Cash" option is selected
    if (cashOption.checked) {
        // Hide the card details form
        cardDetailsForm.style.display = 'none';
    }
});

// Add an event listener to the "Place Order" button
document.getElementById('place-order').addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default form submission
=======
// Get references to the payment method elements
const cardOption = document.getElementById('cards');
const cashOption = document.getElementById('cash');
const ewalletOption = document.getElementById('ewallet');

// Get references to the elements to hide
const qrCodeImage = document.getElementById('qr-code');
const cardDetailsForm = document.querySelector('.card-details-form');

// Function to update visibility based on selected payment method
function updatePaymentMethodVisibility() {
    const selectedPaymentMethod = document.querySelector('input[name="payment-method"]:checked');

    // Hide all elements by default
    qrCodeImage.style.display = 'none';
    cardDetailsForm.style.display = 'none';

    if (selectedPaymentMethod && selectedPaymentMethod.value === 'ewallet') {
        // Show the QR code for E-Wallet
        qrCodeImage.style.display = 'block';
    } else if (selectedPaymentMethod && selectedPaymentMethod.value === 'cards') {
        // Show the card details form for Cards
        cardDetailsForm.style.display = 'block';
    }
}

// Initial check when the page loads
window.addEventListener('load', updatePaymentMethodVisibility);

// Add event listeners to listen for changes in payment methods
const paymentMethodRadios = document.querySelectorAll('input[name="payment-method"]');
paymentMethodRadios.forEach((radio) => {
    radio.addEventListener('change', updatePaymentMethodVisibility);
});

// Get references to the card number and CVV input elements
const cardNumberInput = document.getElementById('card-number');
const cvvInput = document.getElementById('cvv');

// Function to create and add requirement elements below an input field
function addRequirements(inputElement) {
    const requirements = document.createElement('p');
    requirements.classList.add('input-requirements');
    requirements.style.color = 'red';
    inputElement.insertAdjacentElement('afterend', requirements);
    return requirements;
}

// Add requirement elements for card number and CVV fields
const cardNumberRequirements = addRequirements(cardNumberInput);
cardNumberRequirements.textContent = 'Must be a 16-digit number.';
cardNumberRequirements.style.display = 'none';

const cvvRequirements = addRequirements(cvvInput);
cvvRequirements.textContent = 'Must be a 3-digit number.';
cvvRequirements.style.display = 'none';

// Add event listeners for card number and CVV input fields
cardNumberInput.addEventListener('input', () => {
    const isValid = isValidCardNumber(cardNumberInput.value);
    toggleError(cardNumberInput, isValid);
});

cvvInput.addEventListener('input', () => {
    const isValid = isValidCVV(cvvInput.value);
    toggleError(cvvInput, isValid);
});

// Function to validate card number
function isValidCardNumber(cardNumber) {
    return /^\d{16}$/.test(cardNumber);
}

// Function to validate CVV
function isValidCVV(cvv) {
    return /^\d{3}$/.test(cvv);
}

// Function to toggle requirement message and red border
function toggleError(inputElement, isValid) {
    const requirementsElement = inputElement.nextElementSibling;
    if (!isValid) {
        inputElement.style.borderColor = 'red';
        requirementsElement.style.display = 'block'; // Show the requirement message
    } else {
        inputElement.style.borderColor = 'initial';
        requirementsElement.style.display = 'none'; // Hide the requirement message
    }
}




// Add an event listener to the "Place Order" button
document.getElementById('place-order').addEventListener('click', function (e) {
    //e.preventDefault(); // Prevent the default form submission
>>>>>>> MinKhant:FCproject/static_project/scripts/HorngEn_scripts.js

    // Validate Shipping Information
    const nameInput = document.getElementById('name');
    const emailInput = document.getElementById('email');
    const shipAddressInput = document.getElementById('ship-address');
    const shipCityInput = document.getElementById('ship-city');
    const shipPostalCodeInput = document.getElementById('ship-postal-code');
    const phoneInput = document.getElementById('phone');

    // Validation for shipping fields
    let isValid = true; // Flag to track overall validation

    // Helper function to display an error message and turn the field border red
    function displayError(inputElement, errorMessage) {
        const errorElement = document.getElementById(inputElement.id + '-error');
        errorElement.textContent = errorMessage;
        errorElement.style.color = 'red'; // Set the error text color to red
        errorElement.style.display = 'block';
        inputElement.style.borderColor = 'red'; // Set the field border color to red
    }

    // Helper function to hide the error message and restore the field border
    function hideError(inputElement) {
        const errorElement = document.getElementById(inputElement.id + '-error');
        errorElement.textContent = '';
        errorElement.style.display = 'none';
        inputElement.style.borderColor = 'initial'; // Restore the field border color
    }

    function validateField(inputElement, validationFunction, errorMessage) {
        const value = inputElement.value.trim();

        if (!validationFunction(value)) {
            displayError(inputElement, errorMessage);
            isValid = false;
        } else {
            hideError(inputElement);
        }
    }

    // Validation functions
    function isValidName(name) {
        return /^[A-Za-z\s]+$/.test(name);
    }

    function isValidEmail(email) {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    }

    function isValidString(input) {
        return /^[A-Za-z\s]+$/.test(input);
    }

    function isValidPostalCode(postalCode) {
        return /^\d{5}$/.test(postalCode);
    }

    function isValidPhone(phone) {
        return /^\d{1,11}$/.test(phone);
    }

    // Validate specific fields and highlight if empty
    validateField(nameInput, isValidName, 'Please enter a valid name.');
    validateField(emailInput, isValidEmail, 'Please enter a valid email.');
    validateField(shipAddressInput, isValidString, 'Please enter a valid shipping address.');
    validateField(shipCityInput, isValidString, 'Please enter a valid shipping city.');
    validateField(shipPostalCodeInput, isValidPostalCode, 'Please enter a valid postal code (5 digits).');
    validateField(phoneInput, isValidPhone, 'Please enter a valid phone number (up to 11 digits).');

    // Check if overall validation passed
    if (!isValid) {
        alert('Please fill out all required fields correctly.');
        return;
    }

    // If all fields are valid, proceed with the order
<<<<<<< HEAD:main/Scripts/cateringSystem/scripts/HorngEn_scripts.js
    alert('Order placed successfully!');
    // You can submit the form to a server or redirect the user to a confirmation page here
});
=======
    //alert('Order placed successfully!');
    document.getElementsByClassName('details-form').submit();
    // You can submit the form to a server or redirect the user to a confirmation page here
});

// Add an event listener to the "Place Order" button
document.getElementById('place-order').addEventListener('click', function (e) {
    e.preventDefault(); // Prevent the default form submission

    // Validate Shipping Information (your existing validation code)

    let isValid = true; // Flag to track overall validation

    // Validate specific fields and highlight if empty

    // ... (your existing validation code for name, email, address, city, postal code, and phone)

    // Check if overall validation passed
    if (!isValid) {
        alert('Please fill out all required fields correctly.');
        return;
    }

    // If all fields are valid, proceed with the order
    alert('Order placed successfully!');

    // Submit the form
    const form = document.querySelector('.details-form');
    form.submit();

    // Redirect to the track order page (you may need to update the URL)
    //window.location.href = "{% url 'foodcateringapp:trackorderindex' %}";
});
>>>>>>> MinKhant:FCproject/static_project/scripts/HorngEn_scripts.js
