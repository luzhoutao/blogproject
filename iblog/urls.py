from django.conf.urls import url

from . import views

app_name = 'iblog'
urlpatterns = [
    url(r'^index/$', views.index, name="index"),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^search/', views.search, name='search'),
    url(r'^$', views.aboutme, name='aboutme')
]
