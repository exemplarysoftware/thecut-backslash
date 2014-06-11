jQuery(document).ready(function($){

    // add grid class on load
  $('.changelist .results').addClass('grid');

  // toggle grid class
  $('#view-trigger').on('click', function(){
    $('.changelist .results').toggleClass('grid');
  });

});
