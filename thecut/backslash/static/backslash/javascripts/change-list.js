jQuery(document).ready(function($){

  $('#filter-panel-trigger').on('click', function(){

    $('.object-filters').toggleClass('open');

    $(this).text(function(i, text){
      return text === "Show Filters" ? "Hide Filters" : "Show Filters";
    });

  });

});
