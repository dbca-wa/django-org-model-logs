# Generated by Django 3.2.13 on 2022-08-04 07:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org_model_logs', '0003_alter_useraction_unique_together'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='communicationslogentry',
            unique_together=set(),
        ),
    ]
