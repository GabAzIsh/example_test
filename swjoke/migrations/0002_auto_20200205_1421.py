# Generated by Django 3.0.2 on 2020-02-05 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('swjoke', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recruit',
            name='recruit_questions',
            field=models.ManyToManyField(to='swjoke.Test'),
        ),
        migrations.AddField(
            model_name='test',
            name='answer',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3),
        ),
    ]
