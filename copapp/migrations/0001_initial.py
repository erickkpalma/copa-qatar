# Generated by Django 4.1 on 2022-09-10 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TabelaModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time1', models.CharField(max_length=10)),
                ('time2', models.CharField(max_length=10)),
                ('dia', models.IntegerField(blank=True)),
                ('horario', models.DateTimeField()),
            ],
        ),
    ]
