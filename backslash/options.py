from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    change_form_template = 'backslash/change_form.html'
    change_list_template = 'backslash/change_list.html'
    delete_confirmation_template = 'backslash/delete_confirmation.html'
    object_history_template = 'backslash/object_history.html'

