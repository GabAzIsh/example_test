# Generated by Django 3.0.2 on 2020-01-31 08:03

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recruit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('recruit_planet', models.CharField(choices=[('Ashas Ree', 'Ashas Ree'), ('Athiss', 'Athiss'), ('Begeren', 'Begeren'), ('Bosthirda', 'Bosthirda'), ("Ch'hodos", 'Chhodos'), ('Dromund Fels', 'Dromund Fels'), ('Dromund Ixin', 'Dromund Ixin'), ('Dromund Kaas', 'Dromund Kaas'), ('Dromund Kalakar', 'Dromund Kalakar'), ('Kalakar Six', 'Kalakar Six'), ('Dromund Tyne', 'Dromund Tyne'), ('Jaguada', 'Jaguada'), ("Jaguada's moon", 'Jaguadas Moon'), ('Kalsunor', 'Kalsunor'), ('Khar Delba', 'Khar Delba'), ('Khar Shian', 'Khar Shian'), ('Korriban', 'Korriban'), ('Korriz', 'Korriz'), ('Krayiss Two', 'Krayiss Two'), ('Nfolgai', 'Nfolgai'), ('Rhelg', 'Rhelg'), ('Ziost', 'Ziost')], default='Ashas Ree', max_length=20)),
                ('recruit_name', models.CharField(max_length=100)),
                ('recruit_age', models.PositiveIntegerField()),
                ('recruit_email', models.EmailField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Sith',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sith_name', models.CharField(max_length=100)),
                ('sith_planet', models.CharField(choices=[('Ashas Ree', 'Ashas Ree'), ('Athiss', 'Athiss'), ('Begeren', 'Begeren'), ('Bosthirda', 'Bosthirda'), ("Ch'hodos", 'Chhodos'), ('Dromund Fels', 'Dromund Fels'), ('Dromund Ixin', 'Dromund Ixin'), ('Dromund Kaas', 'Dromund Kaas'), ('Dromund Kalakar', 'Dromund Kalakar'), ('Kalakar Six', 'Kalakar Six'), ('Dromund Tyne', 'Dromund Tyne'), ('Jaguada', 'Jaguada'), ("Jaguada's moon", 'Jaguadas Moon'), ('Kalsunor', 'Kalsunor'), ('Khar Delba', 'Khar Delba'), ('Khar Shian', 'Khar Shian'), ('Korriban', 'Korriban'), ('Korriz', 'Korriz'), ('Krayiss Two', 'Krayiss Two'), ('Nfolgai', 'Nfolgai'), ('Rhelg', 'Rhelg'), ('Ziost', 'Ziost')], default='Ashas Ree', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=200)),
                ('unique_sith_order_code', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
