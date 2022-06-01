from django.conf.urls import url
from . import views

urlpatterns = [
    # orders settlement
    url(r'^orders/settlement/$', views.OrderSettlementView.as_view(), name='settlement'),
    # orders payment
    url(r'^orders/commit/$', views.OrderCommitView.as_view()),
    # orders success
    url(r'^orders/success/$', views.OrderSuccessView.as_view()),
]