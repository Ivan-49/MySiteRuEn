from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
class Article(models.Model):
    title = models.CharField(verbose_name=_('title'), max_length=255, null=True, blank=True)
    slug = models.SlugField(verbose_name=_('slug'), unique=True)
    url = models.CharField(verbose_name=_('url'),max_length=255, null=True, blank=True)
    description = models.TextField(verbose_name=_('description'), null=True, blank=True)
    text = models.TextField(verbose_name=_('text'), null=True, blank=True)

    def __str__(self): 
        return self.title
    
    def get_absolute_url(self):
        return reverse('news:article_detail', kwargs={'slug': self.slug})