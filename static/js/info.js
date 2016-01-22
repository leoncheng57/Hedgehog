var sbutton = document.getElementById('submit-button');
sbutton.addEventListener('click', function(e) {
    storeInfo(e, 
	      document.getElementById('info-title').value, 
	      document.getElementById('info-body').value, 
	      document.getElementById('tag-name').value
	     )
});



function storeInfo(e, title, body, tag) {
    if (e.keyCode == 13) {
	$.ajax({
	    type: 'POST',
	    url: '/api/info/create/',
	    data: {title:title, body:body, tag:tag},
	    accepts: 'application/json',
	    success: function(data) {

		console.log("data: "+data);
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
    console.log("storeInfo has been run!");
}
