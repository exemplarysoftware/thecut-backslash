from django.contrib.sites.models import Site


def current_site(request):
    """A context processor to add current site to context."""
    try:
        site = Site.objects.get_current()
    except Site.DoesNotExist:
        site = None
    return {'current_site': site, 'site': site}

