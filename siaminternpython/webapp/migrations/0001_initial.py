# Generated by Django 2.2.6 on 2019-10-21 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(default='', max_length=10)),
                ('Email', models.CharField(default='', max_length=20)),
                ('Dob', models.CharField(default='', max_length=6)),
                ('Mobile_Numer', models.CharField(default='', max_length=10)),
                ('Address', models.TextField(default='')),
            ],
        ),
    ]
