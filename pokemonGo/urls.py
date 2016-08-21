from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pokemonGo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^poke_search/(?P<foo>\w+)', 'search.views.srch', name = 'search'),
    url(r'^searchGET$', 'search.views.srchget', name = 'search'),
    url(r'^searchPOST$', 'search.views.srchpost', name = 'search'),
    url(r'^searchREDIRECT/(?P<search_string>[\*\w\-]+)$', 'search.views.srchredirect', name = 'search'),
    url(r'^searchLISTJS$', 'search.views.srchlistjs', name = 'search'),
)
