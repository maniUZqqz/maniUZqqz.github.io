document.getElementById('submitButton').addEventListener('click', function() {
    var photo = document.getElementById('photo').value;
    var address = document.getElementById('address').value;
    var phone = document.getElementById('phone').value;
    var errorMessage = document.getElementById('errorMessage');

    if (photo === '' || address === '' || phone === '') {
        errorMessage.style.display = 'block';
    } else {
        errorMessage.style.display = 'none';
        document.getElementById('formContainer').style.display = 'none';
    }
})
const image = document.getElementById("IMG")