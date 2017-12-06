from django.conf.urls import url
from service import views

urlpatterns = [
    url(r'^$', views.index, name='/'),
    url(r'^about$', views.about, name='/about'),
    url(r'^contacts$', views.contacts, name='/contacts'),
    url(r'^profile', views.profile, name='/profile'),
    url(r'^services$', views.services, name='/services'),
]