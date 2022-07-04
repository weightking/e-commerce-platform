from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from .views import statistical, users

urlpatterns = [
    # login route
    url(r'^authorizations/$', obtain_jwt_token),
    # statical total route
    url(r'^statistical/total_count/$', statistical.UserTotalCountView.as_view()),
    # day_increment
    url(r'^statistical/day_increment/$', statistical.UserDayCountView.as_view()),
    # day_active
    url(r'^statistical/day_active/$', statistical.UserActiveCountView.as_view()),
    # day_orders
    url(r'^statistical/day_orders/$', statistical.UserOrderCountView.as_view()),
    # month_increment
    url(r'^statistical/month_increment/$', statistical.UserMonthCountView.as_view()),
    # goodsDayView
    url(r'^statistical/goods_day_views/$', statistical.GoodsDayView.as_view()),
    # user management
    url(r'^users/$', users.UserView.as_view()),
]