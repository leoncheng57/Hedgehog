var loginForm = $('#login');
var registerForm = $('#register');
var signoutButton = $('#signout');
var dummyLogin = $('#dummy');

// Assumedly, we're gonna stick some form validation in here.

if (loginForm) loginForm.submit( function(e) {
  // e.preventDefault();
});

if (registerForm) registerForm.submit( function(e) {
  // e.preventDefault();
});

if (signoutButton) signoutButton.click( function(e) {
  console.log("Well this...");
  $('<form action="/api/logout/" method="POST">').submit();
});

if (dummyLogin) dummyLogin.click( function(e) {
  $('<form action="api/login/dummy/" method="POST">').submit();
})