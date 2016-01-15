var loginForm = $('#login')
var registerForm = $('#register')
var signoutButton = $('#signout')

// Assumedly, we're gonna stick some form validation in here.

if (loginForm) loginForm.submit( function(e) {
  // e.preventDefault();
});

if (registerForm) registerForm.submit( function(e) {
  // e.preventDefault();
});

if (signoutButton) signoutButton.submit( function(e) {
  e.target.submit();
});