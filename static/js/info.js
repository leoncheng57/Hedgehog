var createInfo = $('#create-info');
var showButton = $('#showButton');

if (createInfo) createInfo.submit( function(e) {
    e.preventDefault();
    var form = {};
    $.each( $(this).serializeArray(), function(i, e) {
	form[e.name] = e.value;
    });
    $.ajax({
	type: 'POST',
	url: '/api/info/create/',
	data: JSON.stringify(form),
	contentType: 'application/json',
	accepts: 'application/json',
	success: function(data) {
	    console.log(data);
	    
	    // $('#' + type + '-search-results').empty();				       
	    // $.each(data, function(i, item) {					       
	    //     $('#' + type + '-search-results').append(			       
	    // 	  $('<li>').append(item.name + ' (' + item._id.$oid + ')'));	       
	    // });								       
	    
	}
    });
});

if (showButton) showButton.click( function(e) {
    console.log("displaying the infos");
    $('<form action="/api/info/display_infos/" method="POST">').submit();
});

function myFunction() {
    document.getElementById("myP").contentEditable = true;
    //document.getElementById("demo").innerHTML = "STUDY GUIDE IN PROGRESS...";
}
function stop(){
	document.getElementById("myP").contentEditable = false;
}


