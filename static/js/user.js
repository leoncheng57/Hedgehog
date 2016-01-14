var loginForm = $('#login')
var registerForm = $('#register')

// Assumedly, we're gonna stick some form validation in here.

if (loginForm) loginForm.submit( function(e) {
  // e.preventDefault();
});

if (registerForm) registerForm.submit( function(e) {
  e.preventDefault();
});