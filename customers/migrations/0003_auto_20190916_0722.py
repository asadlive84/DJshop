# Generated by Django 2.2.5 on 2019-09-16 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_auto_20190916_0713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerbilling',
            name='total_price',
            field=models.FloatField(null=True),
        ),
    ]
