# Generated by Django 3.2.4 on 2022-11-03 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weatherdata',
            name='precipprob',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='weatherdata',
            name='uvindex',
            field=models.FloatField(),
        ),
    ]