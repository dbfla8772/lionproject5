from django.db import models
from django.contrib.auth.models import AbstractUser 

# Create your models here.
class CustomUser(AbstractUser): #  우리가 만들 usermodel에 AbstractUser를 상속받아서 확장하고 싶은 colmn을 추가함.
    nickname = models.CharField(max_length=100)  # 닉네임
    tel = models.CharField(max_length=13)  # 전화번호(13자리 ex. 010-1111-2222)
    email = models.EmailField()  # 이메일
    university = models.CharField(max_length=50)  # 대학교
    address = models.CharField(max_length=200)  # 주소
