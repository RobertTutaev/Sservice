from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^$', views.index, name='/'),
    url(r'^authenticated$', views.authenticated),
    url(r'^services$', views.services),
    url(r'^databases/(?P<id>\d+)$', views.databases),
    url(r'^service/(?P<id>\d+)/(?P<db>\d+)/(?P<snils>\d{3}-\d{3}-\d{3} \d{2}$)$', views.service),
]
