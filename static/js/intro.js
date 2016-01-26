$(".intro").fadeIn(1000);

$('#logo').click( function homepage() {
    $(".login").fadeOut(1000);
    $(".signup").fadeOut(1000);
    $(".about").fadeOut(1000);
    $(".team").fadeOut(1000);
    $(".intro").fadeIn(1000);
});

$('#signin').click( function signin() {
    $(".intro").fadeOut(1000);
    $(".signup").fadeOut(1000);
    $(".about").fadeOut(1000);
    $(".team").fadeOut(1000);
    $(".login").fadeIn(1000);
});

$('#signup').click( function signup() {
    $(".login").fadeOut(1000);
    $(".intro").fadeOut(1000);
    $(".about").fadeOut(1000);
    $(".team").fadeOut(1000);
    $(".signup").fadeIn(1000);
});

$('#about').click( function about() {
    $(".login").fadeOut(1000);
    $(".intro").fadeOut(1000);
    $(".signup").fadeOut(1000);
    $(".team").fadeOut(1000);
    $(".about").fadeIn(1000);
});

$('#team').click( function team() {
    $(".login").fadeOut(1000);
    $(".intro").fadeOut(1000);
    $(".signup").fadeOut(1000);
    $(".about").fadeOut(1000);
    $(".team").fadeIn(1000);
});