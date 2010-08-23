from busara.busaraadmin.options import ModelAdmin
from django.contrib.admin import sites

class AdminSite(sites.AdminSite):
    actions = []
    index_template = 'busaraadmin/index.html'
    
    def register(self, model_or_iterable, admin_class=None, **options):
        if admin_class is None:
            admin_class = ModelAdmin
        super(AdminSite, self).register(model_or_iterable,
            admin_class=admin_class, **options)

site = AdminSite(name='busaraadmin')

