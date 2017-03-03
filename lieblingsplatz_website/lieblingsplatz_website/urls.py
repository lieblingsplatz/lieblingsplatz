from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    #u rl(r'^$', 'lieblingsplatz_website.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'map.views.home_page', name='home'),
    url(r'^kita/(?P<pk>\d+)/$', 'map.views.kita_detail', name='kita_detail'),
    url(r'^list-kitas$', 'map.views.list_kitas', name='list-kitas'),
    url(r'^admin/', include(admin.site.urls)),
]
