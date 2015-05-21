backslashRequire(

    ['jquery', 'domReady!'],

    function ($) {

        'use strict';

        var $noticesContainer = $('#notices');
        var server = $noticesContainer.attr('data-server'),
            domain = $noticesContainer.attr('data-domain');
        var url = 'https://notices.thecut.net.au/notices.xml' + '?tags=' + server + '&tags=' + domain;

        $.ajax({
            url: url,
            dataType: 'xml',
            crossDomain: true,
            success: function (data) {
                $(data).find('entry').each(function (iteration, Element) {
                    var $entry = $(Element);

                    if (iteration === 0) {
                        $noticesContainer.before($('<h1>').text('Notices'));
                    }

                    var title = $entry.find('title').text();
                    var content = $entry.find('summary').text();
                    var image = $entry.find('link[type="image/jpeg"]');

                    var $li = $('<li>');
                    var $h2 = $('<h2>').text(title);
                    $li.append($h2);

                    if (image) {
                        $li.append($('<img>').attr('src', image.attr('href')));
                    }

                    $noticesContainer.append($li.append(content));
                });
            }
        });

    }

);
