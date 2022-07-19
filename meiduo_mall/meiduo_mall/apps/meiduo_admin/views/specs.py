from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SPUSpecification
from goods.models import SPU
from meiduo_admin.serializers.specs import SPUSpecificationSerializer, SPUSerializer
from meiduo_admin.utils import UserPageNum

class SpecsView(ModelViewSet):

    serializer_class = SPUSpecificationSerializer
    queryset = SPUSpecification.objects.all()
    pagination_class = UserPageNum

    def simple(self, request):
        # get SPU goods information
        spus = SPU.objects.all()
        ser = SPUSerializer(spus, many=True)

        return Response(ser.data)
