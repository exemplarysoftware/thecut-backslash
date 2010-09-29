from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.db import models
from thecut.managers import QuerySetManager
from thecut.utils import generate_unique_slug


class AbstractResource(models.Model):
    """Abstract resource model."""
    title = models.CharField(max_length=200)
    headline = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    
    publish_at = models.DateTimeField('publish date & time',
        help_text='This page will only be viewable on the website \
            if it is enabled, and this date and time has past.')
    is_enabled = models.BooleanField('enabled', default=True)
    is_indexable = models.BooleanField('indexable', default=True,
        help_text='Should this page be indexed by search engines?')
    is_featured = models.BooleanField('featured', default=False)
    meta_description = models.CharField(max_length=200, null=True,
        blank=True, help_text='Optional short description for use by \
            search engines.')
    
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
        ordering = ['title']
    
    class QuerySet(models.query.QuerySet):
        def active(self):
            """Return active (enabled, published) objects."""
            return self.filter(is_enabled=True).filter(
                publish_at__lte=datetime.now())
        
        def featured(self):
            """Return featured objects."""
            return self.filter(is_featured=True)
        
        def indexable(self):
            """Return active, indexable objects."""
            return self.active().filter(is_indexable=True)
    
    def __unicode__(self):
        return self.title
   
    @property
    def is_active(self):
        return self in self.__class__.objects.active().filter(
            pk=self.pk)
    
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
        super(self.__class__, self).save(*args, **kwargs)


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
        super(self.__class__, self).save(*args, **kwargs)

