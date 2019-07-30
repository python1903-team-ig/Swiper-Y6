from random import randrange
import requests
from django.core.cache import cache
from common import keys
from swiper import config

def gen_vcode(length=4):
    start = 10 ** (length-1)
    end = 10 ** length
    return str(randrange(start, end))

def send_sms(phonenum):
    params = config.YZX_SMS_PARAMS.copy()
    params['mobile'] = phonenum

    vcode = gen_vcode()
    params['param'] = vcode
    print('----->', vcode)
    cache.set(keys.VCODE_KEY % phonenum, vcode)

    print(params)
    resp = requests.post(config.YZX_SMS_API, json=params)

    if resp.status_code == 200:
        result = resp.json()
        if result['code'] == '000000':
            return True, result['msg']
        else:
            return False, result['msg']
    else:
        return False, '短信服务器错误'