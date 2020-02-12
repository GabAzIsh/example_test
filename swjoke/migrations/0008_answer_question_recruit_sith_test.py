# Generated by Django 3.0.2 on 2020-02-10 12:57

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('swjoke', '0007_auto_20200210_1554'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
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
                ('shadow_hand', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='swjoke.Sith')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], default='no', max_length=3)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swjoke.Question')),
                ('recruit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='swjoke.Recruit')),
            ],
        ),
    ]