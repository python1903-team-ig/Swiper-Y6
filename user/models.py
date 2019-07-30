from django.db import models
import datetime

class User(models.Model):

    SEX = (
        ('male', "男性"),
        ('female', "女性"),
        ('no sex', "无")
    )

    phonenum = models.CharField(max_length=20, unique=True, verbose_name="手机号")
    nickname = models.CharField(max_length=32, unique=True, verbose_name="昵称")
    sex = models.CharField(max_length=8, choices=SEX, verbose_name="性别")
    birth_year = models.IntegerField(default=2000, verbose_name="出生年")
    birth_month = models.IntegerField(default=1, verbose_name="出生月")
    birth_day = models.IntegerField(default=1, verbose_name="出生日")
    avatar = models.CharField(max_length=256, verbose_name="个人形象url")
    location = models.CharField(max_length=16, verbose_name="常居住地")


    @property
    def age(self):
        today = datetime.date.today()
        birth_data = datetime.date(self.birth_year,self.birth_month,self.birth_day)

        return (today - birth_data).days // 365

    def to_dict(self):
        return {
            'phonenum': self.phonenum,
            'nickname': self.nickname,
            'sex': self.sex,
            'age': self.age,
            'avatar': self.avatar,
            'location': self.location
        }