# Generated by Django 3.2 on 2021-04-25 15:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('HIS', '0002_auto_20210425_2303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='HIS.project', verbose_name='项目编号'),
        ),
    ]
