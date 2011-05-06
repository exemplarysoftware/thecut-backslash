from thecut.backslash.options import ModelAdmin
from django.contrib.admin import sites


class AdminSite(sites.AdminSite):
    actions = []
    index_template = 'backslash/index.html'
    login_template = 'backslash/login.html'
    logout_template = 'backslash/logged_out.html'
    app_index_template = 'backslash/app_index.html'
    password_change_template = 'backslash/password_change_form.html'
    password_change_done_template = 'backslash/password_change_done.html'
    
    def register(self, model_or_iterable, admin_class=None, **options):
        if admin_class is None:
            admin_class = ModelAdmin
        super(AdminSite, self).register(model_or_iterable,
            admin_class=admin_class, **options)

site = AdminSite(name='backslash')

