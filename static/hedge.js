$(document).ready(function() {
    console.log("loaded");
    $(".intro").hide().fadeIn(1000);
    $(".login").hide();
    $(".signup").hide();
});

function homepage(){
    $(".login").fadeOut(1000);
    $(".signup").fadeOut(1000);
    $(".intro").fadeIn(1000);
}
function signin(){
    $(".intro").fadeOut(1000);
    $(".signup").fadeOut(1000);
    $(".login").fadeIn(1000);
}
function signup(){
    $(".login").fadeOut(1000);
    $(".intro").fadeOut(1000);
    $(".signup").fadeIn(1000);
}
function about(){
    $(".login").fadeOut(1000);
    $(".intro").fadeOut(1000);
    $(".signup").fadeOut(1000);
}