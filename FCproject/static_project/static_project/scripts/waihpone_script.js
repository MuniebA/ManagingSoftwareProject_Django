const imageInput = document.getElementById('file');
const previewImage = document.getElementById('preview');
const imageLabel = document.getElementById('imageLabel');

function previewSelectedImage() {
    const file = imageInput.files[0];

    if (file) {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function (e) {
            previewImage.src = e.target.result;
            previewImage.style.display = "inline-block";
        }

        imageLabel.style.display = "none";
    }
}

imageInput.addEventListener('change', previewSelectedImage);