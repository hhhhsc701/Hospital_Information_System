# Generated by Django 3.2 on 2021-05-26 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HIS', '0009_medicine_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='surgery',
            field=models.SmallIntegerField(choices=[(0, '休假'), (1, '星期一'), (2, '星期二'), (3, '星期三'), (4, '星期四'), (5, '星期五'), (6, '星期六'), (7, '星期天')], default=0, verbose_name='坐诊时间'),
        ),
    ]
