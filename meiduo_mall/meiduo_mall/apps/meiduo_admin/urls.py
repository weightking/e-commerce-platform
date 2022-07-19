from django.conf.urls import url
from django.contrib import admin
from rest_framework_jwt.views import obtain_jwt_token
from .views import statistical, users, specs, images, skus
from rest_framework.routers import DefaultRouter

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
    # spec
    url(r'^goods/simple/$', specs.SpecsView.as_view({'get':'simple'})),
    # images
    url(r'^skus/simple/$', images.ImageView.as_view({'get':'simple'})),
    # specializer
    url(r'^goods/(?P<pk>\d+)/specs/$', skus.SKUGoodsView.as_view({'get':'specs'})),
]
# goods specs route
router = DefaultRouter()
router.register('goods/specs',specs.SpecsView, basename='specs')
print(router.urls)
urlpatterns += router.urls

# image route
router = DefaultRouter()
router.register('skus/images',images.ImageView, basename='images')
print(router.urls)
urlpatterns += router.urls

# sku route
router = DefaultRouter()
router.register('skus',skus.SKUGoodsView, basename='skus')
print(router.urls)
urlpatterns += router.urls