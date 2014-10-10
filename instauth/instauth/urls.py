from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'instauth.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^insta/redirect', 'insta.views.redirect_view'),
    url(r'^insta/app', 'insta.views.app'),
    url(r'^insta/logout', 'insta.views.logout'),
)
