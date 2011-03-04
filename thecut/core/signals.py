from datetime import datetime
from django.db.models import Max
from django.contrib.sites.models import Site


def set_site(sender, instance, **kwargs):
    """If not set, set the instance's site value to the current site."""
    from thecut.core.models import AbstractSiteResource
    if issubclass(instance.__class__, AbstractSiteResource):
        try:
            instance.site
        except Site.DoesNotExist:
            instance.site = Site.objects.get_current()


def set_publish_at(sender, instance, **kwargs):
    """If not set, set the instance's publish_at value to now."""
    from thecut.core.models import AbstractBaseResource
    if issubclass(instance.__class__, AbstractBaseResource):
        instance.publish_at = instance.publish_at or datetime.now()


def set_order(sender, instance, **kwargs):
    """If not set, set the instance's order value."""
    from thecut.core.models import OrderMixin
    if issubclass(instance.__class__, OrderMixin) and not instance.pk \
        and not instance.order:
        order = instance.__class__.objects.aggregate(
                order=Max('order')).get('order')
        instance.order = order and order + 1 or 1

