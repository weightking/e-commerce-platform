from django.conf.urls import url
from . import views

urlpatterns = [
    # homepage: '/'
    url(r'^$', views.IndexView.as_view(), name='index'),
]