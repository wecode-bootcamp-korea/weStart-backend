# Generated by Django 3.0.6 on 2020-05-19 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='username',
            field=models.CharField(max_length=200, null=True),
        ),
    ]