from django.conf.urls import url

from . import views

app_name = 'iblog'
urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<pk>[0-9]+)/$', views.category, name='category'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/', views.search, name='search'),
    url(r'^archive/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/', views.archive,name='archive'),
    url(r'^long/profile/$', views.long_profile, name='long_profile'),
    url(r'^$', views.aboutme, name='aboutme')
]
