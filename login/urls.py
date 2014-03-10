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
    url(r'^venuemonk/list/','venuemonk.views.list',name='list'),
    url(r'^venuemonk/add/','venuemonk.views.add_venue',name='add_venue'),
    url(r'^venuemonk/delete/','venuemonk.views.delete_venue',name='delete_venue'),
)
