from django.contrib import admin


class ModelAdmin(admin.ModelAdmin):
    def save_model(self, request, obj, form, change):
        if not change: obj.created_by = request.user
        obj.updated_by = request.user
        return super(ModelAdmin, self).save_model(
            request, obj, form, change)

