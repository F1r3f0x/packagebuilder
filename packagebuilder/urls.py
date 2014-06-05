from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'buildpackage.views.index', name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^oauth_response/$', 'buildpackage.views.oauth_response'),
    url(r'^select_components/(?P<package_id>\d+)/$', 'buildpackage.views.select_components'),
    url(r'^package/(?P<package_id>\d+)/$', 'buildpackage.views.package'),
    url(r'^logout/$', TemplateView.as_view(template_name="logout.html")),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
)
