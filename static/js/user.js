var loginForm = $('#login')
var registerForm = $('#register')

if (loginForm) loginForm.submit( function(e) {
  e.preventDefault();
});

if (registerForm) registerForm.submit( function(e) {
  e.preventDefault();
});