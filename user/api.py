from django.shortcuts import render

from django.core.cache import cache
from lib.http import  render_json
from lib.sms import send_sms
from common import keys
from common import errors
from user.models import  User

def submit_phone(request):
    phone = request.POST.get('phone')
    print(phone)
    send_sms(phone)
    return render_json(None)
