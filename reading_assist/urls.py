from django.conf.urls import patterns, include, url
import views


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'language_learning.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index')
)
