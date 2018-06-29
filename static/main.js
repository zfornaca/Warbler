$().ready(function() {
  $('.like').click(function() {
    console.log('this worked');
    alert('IT WORKS');
  });
});

// DONE
// '.like' is a class I added to users/show.html, line 15
// Joel suggested adding print(response.data) to test routes, and making
// the resulting HTML in Terminal easier to read by (temporarily) disabling
// the debug toolbar, since that toolbar is responsible for most of the HTML.

// TODO:
/*
- add "is_liking" and "is_liked" class methods to users and messages
- prevent duplicate likes in likes table?
- uhhh, I can like my own warbles? that doesn't seem right
- uhhh, "Like" appears even when not logged in? And clicking results in a Flask error. OOPS




*/
