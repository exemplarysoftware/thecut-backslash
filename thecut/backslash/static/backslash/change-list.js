backslashRequire(

    ['jquery', 'domReady!'],

    function ($) {

        'use strict';

        $('#filter-panel-trigger').on('click', function () {
            $('.changelist').toggleClass('tools-open');
        });

    }
);
