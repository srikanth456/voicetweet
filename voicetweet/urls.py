from django.conf.urls import patterns, include, url
from . import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^ct-user/$', views.ct_user, name='ct_user'),
    url(r'^accounts/login/$', views.login, name='vt-login'),
    # url(r'^voicetweet/', include('voicetweet.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
