$(document).ready(function() {
    console.log("loaded");
    $(".intro").hide().fadeIn(1000);
});

function homepage(){
    $(".intro").fadeIn(1000);
}
function signin(){
    $(".intro").fadeOut(1000);
}
function signup(){
    $(".intro").fadeOut(1000);
}
function about(){
    $(".intro").fadeOut(1000);
}