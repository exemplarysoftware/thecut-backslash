from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    change_form_template = 'busaraadmin/change_form.html'
    change_list_template = 'busaraadmin/change_list.html'

