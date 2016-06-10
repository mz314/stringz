from django.conf.urls import patterns
from django.conf.urls import url
from strings import views

urlpatterns = patterns(
                       '',
                       url(r'^$', views.StringsView.as_view(), name='strings'),
                       url(r'^sets$', views.StringSetsView.as_view(), name='string_sets'),
                       url(r'^sets/(?P<set>[a-zA-Z0-9_-]+)$', views.stringset, name='string_set'),
                       )
