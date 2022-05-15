# Generated by Django 3.2.7 on 2022-05-15 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0046_auto_20220425_2004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='quarantined_status',
            field=models.CharField(choices=[('COMPLETED', 'Completed'), ('QUARANTINING', 'Quarantining'), ('HOSPITALIZE_WAITING', 'Hospitalize Waiting'), ('HOSPITALIZE', 'Hospitalize'), ('MOVED', 'Moved')], default='QUARANTINING', max_length=32),
        ),
    ]
