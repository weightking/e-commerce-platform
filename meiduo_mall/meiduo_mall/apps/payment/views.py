from django.shortcuts import render
from django.views import View
from alipay import AliPay, DCAliPay, ISVAliPay
from django.conf import settings
import os

from meiduo_mall.utils.views import LoginRequiredJSONMixin
from orders.models import OrderInfo
from django import http
from meiduo_mall.utils.response_code import RETCODE
from payment.models import Payment
# Create your views here.

# 测试账号：revfsf7522@sandbox.com
class PaymentStatusView(View):
    """保存订单支付结果"""

    def get(self, request):
        # 获取前端传入的请求参数
        query_dict = request.GET
        data = query_dict.dict()
        # 获取并从请求参数中剔除signature
        signature = data.pop('sign')
        # initial parameters
        alipay_public_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys/alipay_public_key.pem")).read()
        app_private_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys/app_private_key.pem")).read()

        # 创建支付宝支付对象
        alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None,  # 默认回调url
            app_private_key_string = app_private_key_string,
            alipay_public_key_string = alipay_public_key_string,
            sign_type="RSA2",
            debug=settings.ALIPAY_DEBUG,
        )
        # 校验这个重定向是否是alipay重定向过来的
        success = alipay.verify(data, signature)
        if success:
            # 读取order_id
            order_id = data.get('out_trade_no')
            # 读取支付宝流水号
            trade_id = data.get('trade_no')
            # 保存Payment模型类数据
            Payment.objects.create(
                order_id=order_id,
                trade_id=trade_id
            )

            # 修改订单状态为待评价
            OrderInfo.objects.filter(order_id=order_id, status=OrderInfo.ORDER_STATUS_ENUM['UNPAID']).update(
                status=OrderInfo.ORDER_STATUS_ENUM["UNCOMMENT"])

            # 响应trade_id
            context = {
                'trade_id':trade_id
            }
            return render(request, 'pay_success.html', context)
        else:
            # 订单支付失败，重定向到我的订单
            return http.HttpResponseForbidden('非法请求')

class PaymentView(LoginRequiredJSONMixin, View):
    """订单支付功能"""

    def get(self,request, order_id):
        # 查询要支付的订单
        user = request.user
        try:
            order = OrderInfo.objects.get(order_id=order_id, user=user, status=OrderInfo.ORDER_STATUS_ENUM['UNPAID'])
        except OrderInfo.DoesNotExist:
            return http.HttpResponseForbidden('订单信息错误')
        # initial parameters
        alipay_public_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys/alipay_public_key.pem")).read()
        app_private_key_string = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "keys/app_private_key.pem")).read()
        # 创建支付宝支付对象
        alipay = AliPay(
            appid=settings.ALIPAY_APPID,
            app_notify_url=None,  # 默认回调url
            app_private_key_string = app_private_key_string,
            alipay_public_key_string = alipay_public_key_string,
            sign_type="RSA2",
            debug=settings.ALIPAY_DEBUG,
        )
        # 生成登录支付宝连接
        order_string = alipay.api_alipay_trade_page_pay(
            out_trade_no=order_id,
            total_amount=str(order.total_amount),
            subject="美多商城%s" % order_id,
            return_url=settings.ALIPAY_RETURN_URL,
        )

        # 响应登录支付宝连接
        # 真实环境电脑网站支付网关：https://openapi.alipay.com/gateway.do? + order_string
        # 沙箱环境电脑网站支付网关：https://openapi.alipaydev.com/gateway.do? + order_string
        alipay_url = settings.ALIPAY_URL + "?" + order_string
        return http.JsonResponse({'code': RETCODE.OK, 'errmsg': 'OK', 'alipay_url': alipay_url})