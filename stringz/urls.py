from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import routers
from strings.views import StringViewSet, StringSetViewSet

router = routers.DefaultRouter()
router.register(r'strings', StringViewSet)
router.register(r'stringsets', StringSetViewSet)

urlpatterns = patterns('',
    url(r'^', include('strings.urls')),
    url(r'^api/', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
) 
