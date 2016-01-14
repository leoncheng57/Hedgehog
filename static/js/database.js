var tagsTable = $('#tags');


function getTags() {
  $.ajax({
    type: 'GET',
    url: '/api/',
  });
}