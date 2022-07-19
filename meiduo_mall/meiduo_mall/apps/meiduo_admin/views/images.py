from django.conf import settings
from fdfs_client.client import Fdfs_client
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from goods.models import SKUImage, SKU
from meiduo_admin.serializers.images import ImageSeriazlier, SKUSerializer
from meiduo_admin.utils import UserPageNum
from rest_framework.permissions import IsAdminUser
from celery_tasks.static_file.tasks import get_detail_html

class ImageView(ModelViewSet):
    # 图片序列化器
    serializer_class = ImageSeriazlier
    # 图片查询集
    queryset = SKUImage.objects.all()
    # 分页
    pagination_class = UserPageNum
    permission_classes = [IsAdminUser]

    def simple(self, request):
        skus = SKU.objects.all()
        ser = SKUSerializer(skus, many=True)
        return Response(ser.data)

    # 重写拓展类的保存业务逻辑
    def create(self, request, *args, **kwargs):
          # 创建FastDFS连接对象
        client = Fdfs_client(settings.FASTDFS_PATH)
        # 获取前端传递的image文件
        data = request.FILES.get('image')
        # 上传图片到fastDFS
        res = client.upload_by_buffer(data.read())
        # 判断是否上传成功
        if res['Status'] != 'Upload successed.':
            return Response(status=403)
        # 获取上传后的路径
        image_url = res['Remote file_id']
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 保存图片
        img = SKUImage.objects.create(sku_id=sku_id, image=image_url)

        # 生成新的详情页页面
        get_detail_html.delay(img.sku.id)
                # 返回结果
        return Response(
            {
                'id': img.id,
                'sku': sku_id,
                'image': img.image.url
            },
            status=201  # 前端需要接受201状态
        )
    def update(self, request, *args, **kwargs):

        # 创建FastDFS连接对象
        client = Fdfs_client(settings.FASTDFS_PATH)
        # 获取前端传递的image文件
        data = request.FILES.get('image')
        # 上传图片到fastDFS
        res = client.upload_by_buffer(data.read())
        # 判断是否上传成功
        if res['Status'] != 'Upload successed.':
            return Response(status=403)
        # 获取上传后的路径
        image_url = res['Remote file_id']
        # 获取sku_id
        sku_id = request.data.get('sku')[0]
        # 查询图片对象
        img=SKUImage.objects.get(id=kwargs['pk'])
        # 更新图片
        img.image=image_url
        img.save()

        # 生成新的详情页页面
        get_detail_html.delay(img.sku.id)
        # 返回结果
        return Response(
            {
                'id': img.id,
                'sku': sku_id,
                'image': img.image.url
            },
            status=201  # 前端需要接受201状态码
        )