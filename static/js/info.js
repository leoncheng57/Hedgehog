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





var tagsTable = $('#tags');
var infoTable = $('#info');

getTags();
getInfo();

function getTags() {
  $.ajax({
    type: 'GET',
    url: '/api/tags/',
    accepts: 'application/json',
    success: function (data) {
      $.each(data, function(i, tag) {
        tagsTable.append(
          $('<tr>').append(
            $('<td>').append(i)
          ).append(
            $('<td>').append(tag.name)
          ).append(
            $('<td>').append(tag._id.$oid)
          )
        );
      });
    }
  });
}

function getInfo() {
  $.ajax({
    type: 'GET',
    url: '/api/info/',
    accepts: 'application/json',
    success: function (data) {
      $.each(data, function(i, info) {
        infoTable.append(
          $('<tr>').append(
            $('<td>').append(i)
          ).append(
            $('<td>').append(info.title)
          ).append(
            $('<td>').append(info.author.$oid)
          ).append(
            $('<td>').append(info.body)
          ).append(
            $('<td>').append(info._id.$oid)
          )
        );
      });
    }
  });
}
