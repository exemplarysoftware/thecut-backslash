jQuery(document).ready(function($) {

    var has_logger = !!(window.console && window.console.log);

    $.ajaxSetup({traditional: true});
    $('body').addClass('js-enabled').ajaxStart(function() {
        $(this).addClass('ajax-loading');
    }).ajaxStop(function() {
        $(this).removeClass('ajax-loading');
    });

    // Email link generation
    $('span.mailto').each(function(){
        exp = $(this).text().search(/\((.*?)\)/) != -1 ? new RegExp(/(.*?) \((.*?)\)/) : new RegExp(/.*/);
        match = exp.exec($(this).text());
        addr = match[1] ? match[1].replace(/ at /,'@').replace(/ dot /g,'.') : match[0].replace(/ at /,'@').replace(/ dot /g,'.');
        emaillink = match[2] ? match[2] : addr;
        subject = $(this).attr('title') ? '?subject='+$(this).attr('title').replace(/ /g,'%20') : '';
        $(this).after('<a href="mailto:'+addr+subject+'">'+ emaillink + '</a>');
        $(this).remove();
    });

    // Disable 'fake' links
    $('a[href="#"]').click(function(event) {
        event.preventDefault();
    });

    // Email link click tracking
    $('a[href ^="mailto:"]').on('click', function(event) {
        var href = $(this).attr('href');
        if (window._gaq) {
            try {
                window._gaq.push(['_trackEvent', 'Email', 'Click', href]);
                if (has_logger) {
                    window._gaq.push(function() {console.log('trackEvent: "Email", "Click", "' + href + '"');});
                }
            } catch(error) {}
        }
    });

    $('body > .header').on('mouseover', function(){
      $('body').addClass('nav-open');
    });

    $('body > .header').on('mouseout', function(){
      $('body').removeClass('nav-open');
    });
});

