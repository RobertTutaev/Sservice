from django.conf.urls import url

from service import views

urlpatterns = [
    url(r'^$', views.index, name='/'),
    url(r'^about', views.about, name='/about'),
]
