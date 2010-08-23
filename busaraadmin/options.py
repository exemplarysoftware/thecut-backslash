from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    change_form_template = 'busaraadmin/change_form.html'
    change_list_template = 'busaraadmin/change_list.html'
    delete_confirmation_template = 'busaraadmin/delete_confirmation.html'
    object_history_template = 'busaraadmin/object_history.html'

