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
    # logout url
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
    # user info pager
    url(r'^info/$', views.UserInfoView.as_view(), name='info'),
    # add email
    url(r'^emails/$', views.EmailView.as_view()),
    # verify email
    url(r'^emails/verification/$', views.VerifyEmailView.as_view()),
    # show address
    url(r'^addresses/$', views.AddressView.as_view(), name='address'),
    # add address
    url(r'^addresses/create/$', views.CreateAddressView.as_view()),
    # update and delete address
    url(r'^addresses/(?P<address_id>\d+)/$', views.UpdateDestroyAddressView.as_view()),
    # set the default address
    url(r'addresses/(?P<address_id>\d+)/default/$', views.DefaultAddressView.as_view()),
    # update address title
    url(r'addresses/(?P<address_id>\d+)/title/$', views.UpdateTitleAddressView.as_view()),
    # update password
    url(r'^password/$', views.ChangePasswordView.as_view(), name='pass'),
]