# Generated by Django 2.0.4 on 2018-04-26 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0003_auto_20180426_0913'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='stakeholder',
            field=models.CharField(blank=True, default='兽医', max_length=150, null=True),
        ),
    ]
