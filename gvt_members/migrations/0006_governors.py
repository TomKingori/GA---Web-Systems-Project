# Generated by Django 4.1 on 2022-11-17 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gvt_members', '0005_national_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Governors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('county', models.CharField(max_length=200, null=True)),
                ('photo', models.ImageField(null=True, upload_to='images/')),
            ],
        ),
    ]
