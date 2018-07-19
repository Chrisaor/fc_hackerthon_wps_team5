# Generated by Django 2.0.7 on 2018-07-19 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SingleTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(blank=True, max_length=200)),
                ('destination', models.CharField(blank=True, max_length=200)),
                ('depart_date', models.DateField(blank=True)),
                ('return_date', models.DateField(blank=True)),
                ('seat_class', models.CharField(choices=[('F', '일등석'), ('N', '일반석'), ('B', '비지니스석'), ('P', '프리미엄 일반석')], max_length=200)),
                ('adult', models.IntegerField()),
                ('children', models.IntegerField()),
                ('infants', models.IntegerField()),
            ],
        ),
    ]
