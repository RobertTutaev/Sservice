from django.conf.urls import url
from service import views

urlpatterns = [
    url(r'^$', views.index, name='/'),
    url(r'^about$', views.about, name='/about'),
    url(r'^contacts$', views.contacts, name='/contacts'),
    url(r'^profile', views.profile, name='/profile'),
    url(r'^service/(?P<id>\d+)$', views.service, name='/service'),
    url(r'^api/help/(?P<id>\d+)$', views.api_help, name='/api/help'),
]