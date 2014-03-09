from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'login.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^login/','register.views.login',name='login'),
    url(r'^logout/','register.views.logout',name = 'logout'),
    url(r'^home/', 'login.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^venue/list/','venue.views.list',name='list'),
    url(r'^venue/add/','venue.views.add',name='add'),
)
