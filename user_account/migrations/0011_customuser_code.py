# Generated by Django 3.2.7 on 2021-11-01 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0010_auto_20211025_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='code',
            field=models.CharField(max_length=18, null=True),
        ),
    ]
