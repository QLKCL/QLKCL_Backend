# Generated by Django 3.2.7 on 2022-03-11 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0012_vaccine_vaccinedose'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pandemic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('quarantine_time_not_vac', models.IntegerField(default=14)),
                ('quarantine_time_vac', models.IntegerField(default=10)),
                ('remain_qt_cc_pos_vac', models.IntegerField(default=10)),
                ('remain_qt_cc_pos_not_vac', models.IntegerField(default=14)),
                ('remain_qt_cc_not_pos_vac', models.IntegerField(default=5)),
                ('remain_qt_cc_not_pos_not_vac', models.IntegerField(default=7)),
                ('remain_qt_pos_vac', models.IntegerField(default=10)),
                ('remain_qt_pos_not_vac', models.IntegerField(default=14)),
                ('test_type_pos_to_neg_vac', models.CharField(choices=[('QUICK', 'Quick'), ('RT-PCR', 'Rt Pcr')], default='QUICK', max_length=32)),
                ('num_test_pos_to_neg_vac', models.IntegerField(default=1)),
                ('test_type_pos_to_neg_not_vac', models.CharField(choices=[('QUICK', 'Quick'), ('RT-PCR', 'Rt Pcr')], default='RT-PCR', max_length=32)),
                ('num_test_pos_to_neg_not_vac', models.IntegerField(default=1)),
                ('test_type_none_to_neg_vac', models.CharField(choices=[('QUICK', 'Quick'), ('RT-PCR', 'Rt Pcr')], default='QUICK', max_length=32)),
                ('num_test_none_to_neg_vac', models.IntegerField(default=1)),
                ('test_type_none_to_neg_not_vac', models.CharField(choices=[('QUICK', 'Quick'), ('RT-PCR', 'Rt Pcr')], default='QUICK', max_length=32)),
                ('num_test_none_to_neg_not_vac', models.IntegerField(default=1)),
                ('num_day_to_close_room', models.IntegerField(default=1)),
            ],
        ),
    ]