document.getElementById('tag-search').addEventListener('keyup', function(e) {tagSearch(e)});

function tagSearch(e) {
  if (e.keyCode == 13) {
    console.log("I got: " + e.target.value)
    $.ajax({
      type: 'GET',
      url: '/request/',
      contentType: 'application/json',
      success: function(data) {
        console.log(data);
      }
    })
  }
}