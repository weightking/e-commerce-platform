from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings
from itsdangerous import BadData

from . import constants

def generate_eccess_token(openid):
    """
    签名openid
    :param openid: 用户的openid
    :return: access_token
    """
    serializer = Serializer(settings.SECRET_KEY, expires_in=constants.ACCESS_TOKEN_EXPIRES)
    data = {'openid': openid}
    token = serializer.dumps(data)
    return token.decode()

def check_access_token(access_token_openid):
    # decode the openid
    serializer = Serializer(settings.SECRET_KEY, expires_in=constants.ACCESS_TOKEN_EXPIRES)
    try:
        data = serializer.load(access_token_openid)
    except BadData:
        return None
    else:
        return data.get('openid')