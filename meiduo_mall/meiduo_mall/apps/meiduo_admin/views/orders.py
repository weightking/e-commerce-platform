from rest_framework.decorators import action
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.orders import OrderSeriazlier
from orders.models import OrderInfo
from meiduo_admin.utils import UserPageNum

class OrdersView(ModelViewSet):
    serializer_class = OrderSeriazlier
    queryset = OrderInfo.objects.all()
    pagination_class = UserPageNum
    #permission define
    permission_classes = [IsAdminUser]

    # 重写get_queryset方法，判断是否传递keyword查询参数
    def get_queryset(self):
          # 提取keyword
        keyword=self.request.query_params.get('keyword')

        if keyword == '' or keyword is None:
            return OrderInfo.objects.all()
        else:
            return OrderInfo.objects.filter(order_id__contains=keyword)

    # 在视图中定义status方法修改订单状态
    @action(methods=['put'], detail=True)
    def status(self, request, pk):
        # 获取订单对象
        try:
            order = self.get_object()
        except:
            return Response({'error':'order id incorrect'})
        # 获取要修改的状态值
        status = request.data.get('status')
        # 修改订单状态
        order.status = status
        order.save()
        # 返回结果
        ser = self.get_serializer(order)
        return Response({
            'order_id': order.order_id,
            'status': status
        })