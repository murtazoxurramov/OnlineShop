# Generated by Django 4.0.3 on 2022-05-17 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Product Title')),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='', verbose_name='Product Image')),
                ('description', models.TextField(verbose_name='Product Description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Product Price')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last Name')),
                ('username', models.CharField(max_length=255, verbose_name='Username')),
                ('email', models.EmailField(max_length=255, verbose_name='Email')),
                ('password', models.CharField(max_length=255, verbose_name='Password')),
                ('mobile', models.CharField(max_length=255, verbose_name='Mobile')),
            ],
        ),
        migrations.CreateModel(
            name='WomenProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255, verbose_name='Size')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Product')),
            ],
        ),
        migrations.CreateModel(
            name='MenProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(max_length=255, verbose_name='Size')),
                ('color', models.CharField(max_length=255, verbose_name='Color')),
                ('quantity', models.IntegerField(verbose_name='Quantity')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.category', verbose_name='Category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product', verbose_name='Product')),
            ],
        ),
    ]