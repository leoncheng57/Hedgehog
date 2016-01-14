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
    url: '/api/tags/', // Because as I began writing this I realized I'd need more functions that I have and I wanna go to bed so no chance of those getting done at the moment.
    accepts: 'application/json',
    success: function (data) {
      $.each(data, function(i, info) {
        infoTable.append(
          $('<tr>').append(
            $('<td>').append(i)
          ).append(
            $('<td>').append('info.title')
          ).append(
            $('<td>').append('info.author')
          ).append(
            $('<td>').append(info._id.$oid)
          )
        );
      });
    }
  });
}