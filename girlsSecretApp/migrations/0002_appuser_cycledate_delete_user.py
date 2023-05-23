# Generated by Django 4.1.7 on 2023-04-26 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('girlsSecretApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='CycleDate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menstrual_cycle_length', models.IntegerField()),
                ('period_date', models.DateField()),
                ('safe_days', models.DateField()),
                ('fertility_days', models.DateField()),
                ('ovulation_day', models.DateField()),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
