from django.conf import settings


def attach_call_to_actions(obj):
    obj.call_to_actions = None
    return obj
if 'thecut.ctas' in settings.INSTALLED_APPS:
    try:
        from thecut.ctas.decorators import attach_call_to_actions
    except ImportError:
        pass
# Compatibility for version 0.01 of ctas app.
elif 'ctas' in settings.INSTALLED_APPS:
    try:
        from ctas.decorators import attach_call_to_actions
    except ImportError:
        pass


def attach_mediaset(obj):
    obj.media = None
    return obj
if 'thecut.media' in settings.INSTALLED_APPS:
    try:
        from thecut.media.decorators import attach_mediaset
    except ImportError:
        pass
# Compatibility for version 0.01 of media app.
elif 'media' in settings.INSTALLED_APPS:
    try:
        from media.decorators import attach_mediaset
    except ImportError:
        pass

