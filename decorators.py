from django.conf import settings


def attach_call_to_actions(obj):
    obj.call_to_actions = None
    return obj
if 'ctas' in settings.INSTALLED_APPS:
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

