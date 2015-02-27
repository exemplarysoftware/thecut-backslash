var backslashRequire = requirejs.config({

    baseUrl: document.querySelector('script[src$="/backslash/lib/require.js"][data-main][data-baseUrl]').getAttribute('data-baseUrl'),

    context: 'backslash',

    paths: {
        'domReady': 'lib/domReady',
        'jquery': 'lib/jquery'
    },

    shim: {
        'jquery': {
            exports: 'jQuery',
            init: function () {
                'use strict';
                return this.jQuery.noConflict();
            }
        }
    }

});


backslashRequire(

    ['jquery', 'domReady!'],

    function ($) {

        'use strict';

        // var has_logger = !!(window.console && window.console.log);

        $.ajaxSetup({traditional: true});

        $('body').addClass('js-enabled').ajaxStart(function () {
            $(this).addClass('ajax-loading');
        }).ajaxStop(function () {
            $(this).removeClass('ajax-loading');
        });

        // Disable 'fake' links
        $('a[href="#"]').click(function (event) {
            event.preventDefault();
        });

        // $('body > .header').on('mouseover', function () {
        //     $('body').addClass('nav-open');
        // });

        // $('body > .header').on('mouseout', function () {
        //     $('body').removeClass('nav-open');
        // });

    }
);
