# Generated by Django 3.2.13 on 2022-09-02 07:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('org_model_logs', '0006_auto_20220902_1357'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entrytype',
            options={'ordering': ['id'], 'verbose_name': 'Entry Type', 'verbose_name_plural': 'Entry Types'},
        ),
    ]
