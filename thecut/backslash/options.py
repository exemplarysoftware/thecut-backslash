from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    def __init__(self, *args, **kwargs):
        super (ModelAdmin, self).__init__(*args, **kwargs)
        app_label = self.model._meta.app_label
        model_name = self.model._meta.object_name.lower()
        
        self.add_form_template = self.add_form_template or [
            'backslash/%s/%s/change_form.html' %(app_label, model_name),
            'backslash/%s/change_form.html' %(app_label),
            'backslash/change_form.html']
        
        self.change_form_template = self.change_form_template or [
            'backslash/%s/%s/change_form.html' %(app_label, model_name),
            'backslash/%s/change_form.html' %(app_label),
            'backslash/change_form.html']
        
        self.change_list_template = self.change_list_template or [
            'backslash/%s/%s/change_list.html' %(app_label, model_name),
            'backslash/%s/change_list.html' %(app_label),
            'backslash/change_list.html']
        
        self.delete_confirmation_template = \
            self.delete_confirmation_template or [
            'backslash/%s/%s/delete_confirmation.html' %(app_label,
                model_name),
            'backslash/%s/delete_confirmation.html' %(app_label),
            'backslash/delete_confirmation.html']
        
        self.delete_selected_confirmation_template = \
            self.delete_selected_confirmation_template or [
            'backslash/%s/%s/delete_selected_confirmation.html' %(app_label,
                model_name),
            'backslash/%s/delete_selected_confirmation.html' %(app_label),
            'backslash/delete_selected_confirmation.html']
        
        self.object_history_template = self.object_history_template or [
            'backslash/%s/%s/object_history.html' %(app_label, model_name),
            'backslash/%s/object_history.html' %(app_label),
            'backslash/object_history.html']

