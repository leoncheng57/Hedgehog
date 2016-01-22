document.getElementById('tags-search').addEventListener('keyup', function(e) {queryDatabase(e, 'tags')});
document.getElementById('info-search').addEventListener('keyup', function(e) {queryDatabase(e, 'info')});

function queryDatabase(e, type) {
  if (e.keyCode == 13) {
    $.ajax({
      type: 'GET',
      url: '/request/',
      data: {type: type},
      accepts: 'application/json',
      success: function(data) {
        $('#' + type + '-search-results').empty();
        $.each(data, function(i, item) {
          $('#' + type + '-search-results').append(
            $('<li>').append(item.name + ' (' + item._id.$oid + ')'));
        });
      }
    });
  }
}
