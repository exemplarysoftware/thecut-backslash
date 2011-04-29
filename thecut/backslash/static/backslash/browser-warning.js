function browserWarning() {
    var message_container = document.createElement('div');
    message_container.setAttribute('id', 'browser-warning');
    message_container.style.position = 'absolute';
    message_container.style.top = '0';
    message_container.style.width = '100%';
    message_container.style.height = '100%';
    message_container.style.backgroundColor = '#a40000';
    message_container.style.color = '#000000'
    
    var message_box = document.createElement('div');
    message_box.style.backgroundColor = '#ffffff';
    message_box.style.color = '#000000';
    message_box.style.width = '600px';
    message_box.style.margin = '200px auto';
    message_box.style.padding = '50px';
    message_box.style.border = 'solid 5px #000000';
    
    message_box.innerHTML = '<h1>Your Web Browser Is Out Of Date</h1><br /><p>In order to use the Backslash administration site you will need to upgrade to a newer version, or use an alternative web browser.</p><br /><p>Supported web browsers are listed below:</p><ul style="margin-left: 30px;"><li><a href="http://www.mozilla.com/firefox/" style="color: #3465a4;">Mozilla Firefox</a> (recommended)</li><li><a href="http://www.google.com/chrome/" style="color: #3465a4;">Google Chrome</a></li><li><a href="http://www.microsoft.com/windows/internet-explorer/" style="color: #3465a4;">Internet Explorer 8+</a></li></ul><br /><br /><p class="contact-info">If you require more information, please contact <a href="http://thecut.net.au/contact" style="color: #3465a4;">The Cut</a>.</p>';
    
    document.body.style.height = '100%';
    
    message_container.appendChild(message_box);
    document.body.appendChild(message_container);
    
    var container = document.getElementById('container');
    document.body.removeChild(container);
}

window.onload = browserWarning;

