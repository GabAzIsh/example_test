# Generated by Django 3.0.2 on 2020-02-06 06:47

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('swjoke', '0004_auto_20200206_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('answer', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='SithPlanets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('planet_name', models.CharField(max_length=40, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unique_sith_order_code', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('questions', models.ManyToManyField(blank=True, to='swjoke.Question')),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sith_name', models.CharField(max_length=100)),
                ('sith_planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swjoke.SithPlanets')),
            ],
        ),
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit_name', models.CharField(max_length=100)),
                ('recruit_age', models.PositiveIntegerField()),
                ('recruit_email', models.EmailField(max_length=100)),
                ('recruit_planet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swjoke.SithPlanets')),
                ('recruit_test', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='swjoke.Test')),
            ],
        ),
    ]
