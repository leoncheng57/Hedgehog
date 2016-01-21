document.getElementById('submit-button').addEventListener('keyup', function(e) {queryDatabase(e,
											      document.getElementById('info-title'), 											      document.getElementById('info-body'), 
											      document.getElementById('tag-name'),)});


function storeInfo(e, title, body, tag) {
    if (e.keyCode == 13) {
	$.ajax({
      type: 'POST',
      url: '/api/info/create/',
      data: {title:title, body:body, tag:tag},
      accepts: 'application/json',
      success: function(data) {
	  
	  ///////////////////////////////////////////////////////////////////////////////
          // $('#' + type + '-search-results').empty();				       //
          // $.each(data, function(i, item) {					       //
          //     $('#' + type + '-search-results').append(			       //
	  // 	  $('<li>').append(item.name + ' (' + item._id.$oid + ')'));	       //
          // });								       //
          ///////////////////////////////////////////////////////////////////////////////

      }
    });
  }
}
