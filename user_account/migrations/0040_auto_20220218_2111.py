# Generated by Django 3.2.7 on 2022-02-18 14:11

from django.db import migrations
from utils.enums import MemberQuarantinedStatus, MemberLabel

def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    Member = apps.get_model("user_account", "Member")
    db_alias = schema_editor.connection.alias
    members = Member.objects.using(db_alias).filter(quarantined_status__in=[MemberQuarantinedStatus.QUARANTINING, MemberQuarantinedStatus.REQUARANTINING]).filter(label=MemberLabel.F0)
    for member in list(members):
        if member.positive_test_now != True:
            member.label = MemberLabel.F1
            member.save()

def reverse_func(apps, schema_editor):
    ...

class Migration(migrations.Migration):

    dependencies = [
        ('user_account', '0039_alter_member_label'),
    ]

    operations = [
        migrations.RunPython(forwards_func, reverse_func),
    ]
