# Generated by Django 3.2.5 on 2021-07-30 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('machines', '0002_rename_pessoa_machine'),
    ]

    operations = [
        migrations.AddField(
            model_name='machine',
            name='consumption',
            field=models.CharField(default='0', max_length=200),
        ),
    ]
