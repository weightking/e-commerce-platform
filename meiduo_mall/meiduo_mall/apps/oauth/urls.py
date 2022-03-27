from django.conf.urls import url

from . import views

urlpatterns = [
    # QQ scan login page
    url(r'^qq/login/$', views.QQAuthURLView.as_view()),
    # Authorization Code
    url(r'^oauth_callback/$', views.QQAuthUserView.as_view()),
]