# Generated by Django 3.2.7 on 2021-10-22 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0004_alter_member_background_disease'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='customuser',
            name='staff',
            field=models.BooleanField(default=False),
        ),
    ]