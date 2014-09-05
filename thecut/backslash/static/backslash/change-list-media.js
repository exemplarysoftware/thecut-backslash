backslashRequire(

    ['jquery', 'domReady!'],

    function ($) {

        'use strict';

        // remove 'hidden' class from 'view-trigger' container.
        $('.object-toolbar .hidden').removeClass('hidden');

        // Add grid class on load
        $('.changelist .results').addClass('grid');

        // Toggle grid class
        $('#view-trigger').on('click', function () {
            $('.changelist .results').toggleClass('grid');
            // Toggle label on trigger
            $(this).text(function (i, text) {
                return text === 'Switch to List View' ? 'Switch to Grid View' : 'Switch to List View';
            });
        });

    }
);
