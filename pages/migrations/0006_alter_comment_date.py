# Generated by Django 4.1.2 on 2022-10-14 17:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_alter_comment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.date(2022, 10, 14), verbose_name='Date'),
        ),
    ]