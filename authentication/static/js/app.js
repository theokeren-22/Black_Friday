function togglePassword() {
    var passwordInput = document.getElementById('password');
    var toggleIcon = document.querySelector('.toggle-password');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text'; // Show password
        toggleIcon.classList.remove('fa-eye-slash'); // Remove eye-slash
        toggleIcon.classList.add('fa-eye'); // Add eye
    } else {
        passwordInput.type = 'password'; // Hide password
        toggleIcon.classList.remove('fa-eye'); // Remove eye
        toggleIcon.classList.add('fa-eye-slash'); // Add eye-slash
    }
}

function toggleConfirmPassword() {
    var passwordInput = document.getElementById('confirm_password');
    var toggleIcon = document.querySelector('.toggle-confirm-password');
    
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text'; // Show password
        toggleIcon.classList.remove('fa-eye-slash'); // Remove eye-slash
        toggleIcon.classList.add('fa-eye'); // Add eye
    } else {
        passwordInput.type = 'password'; // Hide password
        toggleIcon.classList.remove('fa-eye'); // Remove eye
        toggleIcon.classList.add('fa-eye-slash'); // Add eye-slash
    }
}
