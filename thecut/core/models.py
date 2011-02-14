from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models
from tagging.fields import TagField
from thecut.core.decorators import attach_call_to_actions, attach_mediaset
from thecut.core.managers import QuerySetManager
from thecut.core.signals import set_order, set_publish_at, set_site
from thecut.core.utils import generate_unique_slug


class OrderMixin(models.Model):
    order = models.PositiveIntegerField(default=0)
    
    class Meta:
        abstract = True
    
    def __init__(self, *args, **kwargs):
        super(OrderMixin, self).__init__(*args, **kwargs)
        ordering = getattr(self.__class__.Meta, 'ordering', [])
        self.__class__.Meta.ordering = ['order'] + ordering

models.signals.post_init.connect(set_order)


class AbstractBaseResource(models.Model):
    """Abstract base resource model."""
    is_enabled = models.BooleanField('enabled', default=True)
    is_featured = models.BooleanField('featured', default=False)
    
    publish_at = models.DateTimeField('publish date & time',
        help_text='This item will only be viewable on the website \
            if it is enabled, and this date and time has past.')
    expire_at = models.DateTimeField('expiry date & time',
        null=True, blank=True,
        help_text='This item will no longer be viewable on the \
            website if this date and time has past. Leave blank if \
            you do not wish this item to expire.')
    publish_by = models.ForeignKey(User,
        related_name='%(class)s_publish_by_user', null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    created_by = models.ForeignKey(User, editable=False,
        related_name='%(class)s_created_by_user')
    
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    updated_by = models.ForeignKey(User, editable=False,
        related_name='%(class)s_updated_by_user')
    
    objects = QuerySetManager()
    
    class Meta:
        abstract = True
        get_latest_by = 'publish_at'
        ordering = ['-created_at']
    
    class QuerySet(models.query.QuerySet):
        def active(self):
            """Return active (enabled, published) objects."""
            now = datetime.now()
            return self.filter(is_enabled=True).filter(
                models.Q(publish_at__lte=now),
                models.Q(expire_at__isnull=True) |
                models.Q(expire_at__gte=now))
        
        def featured(self):
            """Return featured objects."""
            return self.filter(is_featured=True)
    
    @property
    def is_active(self):
        return self in self.__class__.objects.active().filter(
            pk=self.pk)

models.signals.post_init.connect(set_publish_at)


@attach_call_to_actions
@attach_mediaset
class AbstractResource(AbstractBaseResource):
    """Abstract resource model."""
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    
    is_indexable = models.BooleanField('indexable', default=True,
        help_text='Should this page be indexed by search engines?')
    meta_description = models.CharField(max_length=200, null=True,
        blank=True, help_text='Optional short description for use by \
            search engines.')
    tags = TagField(null=True, blank=True, help_text='Separate tags \
        with spaces, put quotes around multiple-word tags.')
    
    template = models.CharField(max_length=100, null=True, blank=True,
        help_text='Example: "app/model_detail.html".')    
    
    objects = QuerySetManager()
    
    class Meta(AbstractBaseResource.Meta):
        abstract = True
        ordering = ['title']
    
    class QuerySet(AbstractBaseResource.QuerySet):
        def indexable(self):
            """Return active, indexable objects."""
            return self.active().filter(is_indexable=True)
    
    def __unicode__(self):
        return self.title
    
    @property
    def heading(self):
        return self.headline and self.headline or self.title


class AbstractSiteResource(AbstractResource):
    """Abstract resource model with a relationship to a site."""
    site = models.ForeignKey(Site)
    
    objects = QuerySetManager()
    
    class Meta(AbstractResource.Meta):
        abstract = True
    
    class QuerySet(AbstractResource.QuerySet):
        def current_site(self):
            """Return objects for the current site."""
            site = Site.objects.get_current()
            return self.filter(site=site)

models.signals.post_init.connect(set_site)


class AbstractSiteResourceWithSlug(AbstractSiteResource):
    """"Abstract site resource model with a slug."""
    slug = models.SlugField()
    
    objects = QuerySetManager()
    
    class Meta(AbstractSiteResource.Meta):
        abstract = True
        unique_together = ['site', 'slug']
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self.title,
                self.__class__, queryset=self.__class__.objects.filter(
                site=self.site))
        super(AbstractSiteResourceWithSlug, self).save(*args, **kwargs)


class AbstractSitesResource(AbstractResource):
    """Abstract resource model with a relationship to many sites."""
    sites = models.ManyToManyField(Site, null=True, blank=True)
    
    objects = QuerySetManager()
    
    class Meta(AbstractResource.Meta):
        abstract = True
    
    class QuerySet(AbstractResource.QuerySet):
        def current_site(self):
            """Return objects for the current site."""
            site = Site.objects.get_current()
            return self.filter(sites=site)


class AbstractSitesResourceWithSlug(AbstractSitesResource):
    """"Abstract sites resource model with a unique slug."""
    slug = models.SlugField(unique=True)
    
    objects = QuerySetManager()
    
    class Meta(AbstractSitesResource.Meta):
        abstract = True
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = generate_unique_slug(self.title,
                self.__class__)
        super(AbstractSitesResourceWithSlug, self).save(*args, **kwargs)

