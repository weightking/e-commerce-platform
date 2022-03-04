from django.conf.urls import url
from . import views

urlpatterns = [
    # 注册
    url(r'^register/$', views.RegisterView.as_view(), name='register'),
    # to check whether the username repeat registration
    url(r'^usernames/(?P<username>[a-zA-Z0-9_-]{5,20})/count/$', views.UsernameCountView.as_view()),
    # to check whether the mobile number repeat registration
    url(r'^mobiles/(?P<mobile>1[3-9]\d{9})/count/$', views.MobileCountView.as_view()),
    # login page url
    url(r'^login/$', views.LoginView.as_view(), name='login'),
]