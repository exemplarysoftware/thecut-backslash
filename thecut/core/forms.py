from datetime import datetime
from django import forms
from django.db.models import Max
from django.contrib.sites.models import Site


class ModelAdminForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelAdminForm, self).__init__(*args, **kwargs)
        if self.fields.get('publish_at', False):
            self.fields['publish_at'].initial = datetime.now()
        if self.fields.get('site', False):
            self.fields['site'].initial = Site.objects.get_current()
        if self.fields.get('sites', False):
            self.fields['sites'].initial = [Site.objects.get_current()]
        if self.fields.get('order', False):
            self.fields['order'].initial = self.Meta.model.objects.aggregate(
                order=Max('order')).get('order', 0) + 1

