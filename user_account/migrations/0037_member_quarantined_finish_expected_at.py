# Generated by Django 3.2.7 on 2022-02-11 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0036_alter_member_quarantined_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='quarantined_finish_expected_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
