# Generated by Django 4.1.4 on 2023-08-21 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calculator_app', '0002_fileupload'),
    ]

    operations = [
        migrations.CreateModel(
            name='emp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empname', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('comname', models.CharField(max_length=200)),
                ('designation', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]