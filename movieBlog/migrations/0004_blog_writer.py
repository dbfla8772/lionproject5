# Generated by Django 3.1.7 on 2021-05-21 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movieBlog', '0003_auto_20210521_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='writer',
            field=models.CharField(max_length=30, null='True'),
            preserve_default='True',
        ),
    ]