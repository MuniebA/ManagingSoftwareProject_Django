// Get references to the card payment options and card details form
const cardOption = document.getElementById('cards');
const cardDetailsForm = document.querySelector('.card-details-form');

// Add an event listener to the card payment options
cardOption.addEventListener('change', () => {
    // Check if a card payment option is selected
    if (cardOption.checked) {
        // Show the card details form
        cardDetailsForm.style.display = 'block';
    } else {
        // Hide the card details form if another option is selected
        cardDetailsForm.style.display = 'none';
    }
});

// Get references to the payment method and QR code image elements
const paymentMethodInput = document.getElementById('ewallet');
const qrCodeImage = document.getElementById('qr-code');

// Add an event listener to the payment method input
paymentMethodInput.addEventListener('change', () => {
    // Check if the "E-Wallet" option is selected
    if (paymentMethodInput.checked) {
        // Show the QR code image
        qrCodeImage.style.display = 'block';
    } else {
        // Hide the QR code image if another option is selected
        qrCodeImage.style.display = 'none';
    }
});