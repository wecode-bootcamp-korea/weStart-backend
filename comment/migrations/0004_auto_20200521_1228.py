# Generated by Django 3.0.6 on 2020-05-21 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0003_auto_20200519_1416'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='username',
        ),
    ]
