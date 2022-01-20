# Generated by Django 3.2.7 on 2022-01-19 17:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.TextField(blank=True, null=True)),
                ('url', models.CharField(blank=True, max_length=2083, null=True)),
                ('type', models.CharField(choices=[('PUSH', 'Push'), ('EMAIL', 'Email'), ('SMS', 'Sms')], default='PUSH', max_length=32)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('created_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='notification_x_created_by', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserNotification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_read', models.BooleanField(default=False)),
                ('notification', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification_x_notification', to='notification.notification')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification_x_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]