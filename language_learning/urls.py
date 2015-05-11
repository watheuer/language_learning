from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'language_learning.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^admin/', include(admin.site.urls)),
    url(r'^', include('reading_assist.urls', namespace='reading'))
)
