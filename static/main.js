$().ready(function() {
  // $('.like').click(function() {
  //   console.log('this worked');
  //   alert('IT WORKS');
  // });

  $('.like').click(function(e) {
    let userId = $(e.target).attr('data-userid');
    let messageId = $(e.target).attr('data-messageid');

    let likeOrUnlike = $(e.target)
      .text() // innerText
      .trim() // get rid of whitespace
      .toLowerCase(); // make it lowercase for the route

    let route = `/users/${userId}/messages/${messageId}/${likeOrUnlike}`;
    console.log(route);

    $.post(route, function(data) {
      $(e.target).toggleClass('btn-primary btn-outline-primary');
      if (likeOrUnlike === 'like') {
        $(e.target).text('Unlike');
      } else {
        $(e.target).text('Like');
      }
    });
  });
});

// DONE

// TODO:
/*
- on click:
  - once that update happens, swap button look/behavior
  - do we just delete the entire form and then append the entire other form?


*/
