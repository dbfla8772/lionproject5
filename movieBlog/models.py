from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator 
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.
class Blog(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=200) # 영화제목
    director = models.CharField(max_length=100) # 감독이름
    rel_date = models.CharField(max_length=10) # 개봉날짜 (년도, 월, 일 합해서 10자리 ex. 2021/01/01)
    writer = models.CharField(max_length=30) # 글쓴이
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)]) # 평점(1점~5점)
    review = models.TextField() # 영화리뷰
    photo = models.ImageField(upload_to='movieBlog/', blank=False, null=False)  # 포스터 사진
    image_thumbnail = ImageSpecField(source = 'photo',processors=[ResizeToFill(120,100)], format="JPEG", options={'quality':60})  # 썸네일

    def __str__(self):
        return self.title

    def summary(self):
        return self.review[:100]  