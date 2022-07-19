from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser
from datetime import date

from rest_framework.viewsets import ModelViewSet

from meiduo_admin.serializers.skus import SKUGoodsSerializer, SKUCategorieSerializer, SPUSpecSerialzier
from meiduo_admin.utils import UserPageNum

from users.models import User
from goods.models import GoodsVisitCount, SKU, GoodsCategory, SPU


class SKUGoodsView(ModelViewSet):
    # 指定序列化器
    serializer_class =SKUGoodsSerializer
    # 指定分页器 进行分页返回
    pagination_class = UserPageNum
    #permission define
    permission_classes = [IsAdminUser]
    # 重写get_queryset方法，判断是否传递keyword查询参数
    def get_queryset(self):
          # 提取keyword
        keyword=self.request.query_params.get('keyword')

        if keyword == '' or keyword is None:
            return SKU.objects.all()
        else:
            return SKU.objects.filter(name__contains=keyword)

    @action(methods=['get'], detail=False)
    def categories(self, request):
        data = GoodsCategory.objects.filter(parent_id__gt=37)
        ser = SKUCategorieSerializer(data, many=True)
        return Response(ser.data)

    def specs(self, request, pk):
        spu = SPU.objects.get(id=pk)
        data = spu.specs.all()
        ser = SPUSpecSerialzier(data, many=True)
        return Response(ser.data)