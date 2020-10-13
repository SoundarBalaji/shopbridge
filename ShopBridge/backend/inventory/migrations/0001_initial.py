# Generated by Django 3.1.1 on 2020-09-29 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000, null=True)),
                ('price', models.IntegerField()),
                ('product_image', models.ImageField(null=True, upload_to='')),
            ],
        ),
    ]
