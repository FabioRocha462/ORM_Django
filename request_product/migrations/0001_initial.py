# Generated by Django 4.1.3 on 2022-11-06 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        ('request', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request_Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='request.request')),
            ],
        ),
    ]
