from rest_framework.generics import ListCreateAPIView
from meiduo_admin.serializers.users import UserSerializer,UserAddSerializer
from meiduo_admin.utils import UserPageNum
from users.models import User


class UserView(ListCreateAPIView):
    # 根据不同的请求方式返回不同序列化器
    def get_serializer_class(self):
        # 请求方式是GET，则是获取用户数据返回UserSerializer
        if self.request.method == 'GET':
            return UserSerializer
        else:
            # POST请求，完成保存用户，返回UserAddSerializer
            return UserAddSerializer
    # 指定分页器
    pagination_class = UserPageNum

    # 重写get_queryset方法，根据前端是否传递keyword值返回不同查询结果
    def get_queryset(self):
        # 获取前端传递的keyword值
        keyword = self.request.query_params.get('keyword')
        # 如果keyword是空字符，则说明要获取所有用户数据
        if keyword is '' or keyword is None:
            return User.objects.all()
        else:
            return User.objects.filter(username__contains=keyword)