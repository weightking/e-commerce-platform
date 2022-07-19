from rest_framework import serializers
from goods.models import SPUSpecification
from goods.models import SPU

class SPUSpecificationSerializer(serializers.ModelSerializer):
    # 关联嵌套返回spu表的商品名
    spu = serializers.StringRelatedField(read_only=True)
    # 返回关联spu的id值
    spu_id = serializers.IntegerField()

    class Meta:
        model = SPUSpecification  # 商品规格表关联了spu表的外键spu
        fields = '__all__'

class SPUSerializer(serializers.ModelSerializer):

    class Meta:
        model = SPU
        fields = ('id', 'name')