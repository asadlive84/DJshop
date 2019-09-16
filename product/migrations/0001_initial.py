# Generated by Django 2.2.5 on 2019-09-16 06:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('ratio', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('image', models.ImageField(default='product.png', upload_to='product/')),
                ('description', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('quantity', models.IntegerField(default=0)),
                ('purchase_price', models.FloatField()),
                ('sales_price', models.FloatField()),
                ('product_type', models.CharField(choices=[('Cn', 'Consumable'), ('St', 'Storable'), ('Se', 'Service')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('measure', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Measure')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
