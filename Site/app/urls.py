from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import JavaScriptCatalog

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
]+i18n_patterns(
    path('', include('news.urls', namespace='news')),
    path('i18n/', include('django.conf.urls.i18n')),
    path('jsi18n', JavaScriptCatalog.as_view(), name='javascript_catalog'),

    prefix_default_language=False
)
