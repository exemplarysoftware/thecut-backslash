from django import template
from django.conf import settings


register = template.Library()

@register.inclusion_tag('backslash/_menu.html', takes_context=True)
def backslash_menu(context):
    backslash_menu_setting = getattr(settings, 'BACKSLASH_MENU', False)
    if backslash_menu_setting:
        module_string = '.'.join(backslash_menu_setting.split('.')[:-1])
        var_string = backslash_menu_setting.split('.')[-1]
        module = __import__(module_string, globals(), locals(), [var_string])
        backslash_menu = getattr(module, var_string)
    else:
        backslash_menu = None
    context.update({'backslash_menu': backslash_menu})
    return context

