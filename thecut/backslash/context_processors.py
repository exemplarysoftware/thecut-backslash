from django.conf import settings
from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from django.utils.text import capfirst
from thecut import backslash


site = backslash.site

def applist(request):
    # http://djangosnippets.org/snippets/1921/
    app_dict = {}
    user = request.user
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        has_module_perms = user.has_module_perms(app_label)
    
        if has_module_perms:
            perms = model_admin.get_model_perms(request)
      
            if True in perms.values():
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'admin_url': mark_safe('/admin/%s/%s/' % (app_label, model.__name__.lower())),
                    'perms': perms}
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    app_dict[app_label] = {
                      'name': app_label.title(),
                      'app_url': app_label + '/',
                      'has_module_perms': has_module_perms,
                      'models': [model_dict]}
    
    app_list = app_dict.values()
    app_list.sort(lambda x, y: cmp(x['name'], y['name']))
    return {'adm_app_list': app_list}


def model_list(request):
    model_list = []
    user = request.user
    for model, model_admin in site._registry.items():
        perms = model_admin.get_model_perms(request)
        if True in perms.values():
            app_label = model._meta.app_label
            model_name = model.__name__.lower()
            model_list += [{'app_label': app_label,
                'model_name': model_name,
                'name': capfirst(model._meta.verbose_name_plural),
                'url': reverse('backslash:%(app_label)s_%(model_name)s_changelist' %({'app_label': app_label, 'model_name': model_name}))}]
    model_list.sort(lambda x, y: cmp(x['name'], y['name']))
    
    order = getattr(settings, 'BACKSLASH_MODEL_ORDER', [])
    order.reverse()
    for item in order:
        app_label, model_name = item.lower().split('.')
        for model_dict in model_list:
            if model_dict['app_label'] == app_label \
                and model_dict['model_name'] == model_name:
                model_list.remove(model_dict)
                model_list.insert(0, model_dict)
    
    return {'backslash_model_list': model_list}

