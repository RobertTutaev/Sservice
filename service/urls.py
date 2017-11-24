from django.conf.urls import url

from service import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^about', views.about),
]
