# Generated by Django 4.1.3 on 2022-11-06 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('locality', models.CharField(max_length=255)),
                ('local', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=10)),
                ('cep', models.CharField(max_length=15)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=15)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]