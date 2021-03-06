# Generated by Django 2.0.5 on 2018-05-09 04:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Consumption',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField()),
                ('consumption', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumption.Area')),
                ('tariff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='consumption.Tariff')),
            ],
        ),
        migrations.AddField(
            model_name='consumption',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='consumption.User'),
        ),
    ]
