# Generated by Django 2.2.13 on 2020-07-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instances', '0007_auto_20200624_0821'),
    ]

    operations = [
        migrations.AlterField(
            model_name='instance',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='created'),
        ),
    ]
