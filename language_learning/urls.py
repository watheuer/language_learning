from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'language_learning.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', include('reading_assist.urls', namespace='reading'))
)
