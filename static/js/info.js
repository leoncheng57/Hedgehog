var createInfo = $('#create-info');
var showButton = $('#showButton');
var tagsTable = $('#tags');
var infoTable = $('#info');

if (tagsTable) getTags();
if (infoTable) getInfo();

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
    }
  });
});

if (showButton) showButton.click( function(e) {
  console.log("displaying the infos");
  $('<form action="/api/info/display_infos/" method="POST">').submit();
});

function myFunction() {
    $('#myP').contentEditable = true;
    //document.getElementById("demo").innerHTML = "STUDY GUIDE IN PROGRESS...";
}

function stop(){
	$('#myP').contentEditable = false;
}

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
            $('<td>').append(info.body)
          )
        );
      });
    }
  });
}
