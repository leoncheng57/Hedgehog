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