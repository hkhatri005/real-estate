# Generated by Django 2.2.5 on 2019-09-28 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_property_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=30)),
            ],
        ),
    ]