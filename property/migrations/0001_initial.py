# Generated by Django 2.2.5 on 2019-09-28 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('property_type', models.CharField(choices=[('S', 'sale'), ('R', 'rent')], max_length=10)),
                ('price', models.IntegerField()),
                ('area', models.DecimalField(decimal_places=2, max_digits=5)),
                ('beds_number', models.PositiveIntegerField()),
                ('baths_number', models.PositiveIntegerField()),
                ('garages_number', models.PositiveIntegerField()),
            ],
        ),
    ]