django.jQuery(document).ready(function($) {

    var $noticesContainer = $('#notices');
    var server = $noticesContainer.attr('data-server');
    var domain = $noticesContainer.attr('data-domain');
    //var url = 'https://notices.thecut.net.au/notices.xml' + '?tags=' + server + '&tags=' + domain;
    var url = 'http://127.0.0.1:8000/notices.xml' + '?tags=' + server + '&tags=' + domain;
    console.log(url);
    $.ajax({
	url: url,
	dataType: 'xml',
	crossDomain: true,
	success: function( data ) {

	    $(data).find('entry').each(function(iteration) {
		if (iteration == 0) {
		    $noticesContainer.before($('<h1>').text('Notices'));
		}

		var title = $(this).find('title').text();
		var content = $(this).find('summary').text();
		var image = $(this).find('link[type="image/jpeg"]')

		var $li = $('<li>')
		var $h2 = $('<h2>').text(title);
		$li.append($h2);

		if ( image != null ) {
		    $li.append($('<img>').attr('src', image.attr('href')));
		}

		$noticesContainer.append($li.append(content));
	    })
	}
    })

});
