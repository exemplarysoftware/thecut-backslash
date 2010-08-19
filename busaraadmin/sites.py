from django.contrib.admin import sites

class AdminSite(sites.AdminSite):
    index_template = 'busaraadmin/index.html'

site = AdminSite(name='busaraadmin')

