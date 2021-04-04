# Generated by Django 3.1.7 on 2021-04-04 11:28

from django.db import migrations, models
import django.db.models.deletion
import index.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Quote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fistName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=index.models.get_image_filename, verbose_name='Image')),
                ('quote', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='index.quote')),
            ],
        ),
    ]