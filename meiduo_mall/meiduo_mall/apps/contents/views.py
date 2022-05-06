from collections import OrderedDict

from django.shortcuts import render
from django.views import View

from contents.models import ContentCategory
from contents.utils import get_categories
# Create your views here.

class IndexView(View):

    def get(self, request):
        # 查询商品频道和分类
        categories = get_categories()
        # search advertisement group
        contents = {}
        content_categories = ContentCategory.objects.all()
        for cat in content_categories:
            contents[cat.key] = cat.content_set.filter(status=True).order_by('sequence')
        # 渲染模板的上下文
        context = {
            'categories': categories,
            'contents': contents,
        }
        return render(request, 'index.html', context)