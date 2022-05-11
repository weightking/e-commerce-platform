from django.conf.urls import url
from . import views

urlpatterns = [
    # homepage: '/'
    url(r'^list/(?P<category_id>\d+)/(?P<page_num>\d+)/$', views.ListView.as_view(), name='list'),
    # hot sort
    url(r'^hot/(?P<category_id>\d+)/$', views.HotGoodsView.as_view()),
    # detail page
    url(r'^detail/(?P<sku_id>\d+)/$', views.DetailView.as_view(), name='detail'),
    # category count
    url(r'^detail/visit/(?P<category_id>\d+)/$', views.DetailVisitView.as_view()),
]