# Generated by Django 3.0.2 on 2020-02-10 19:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('swjoke', '0008_answer_question_recruit_sith_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='planet',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='test', to='swjoke.SithPlanets'),
        ),
    ]
