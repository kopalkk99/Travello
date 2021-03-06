# Generated by Django 3.2.5 on 2021-12-26 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destination',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destName', models.CharField(max_length=200)),
                ('destDesc', models.TextField(verbose_name=2000)),
                ('price', models.IntegerField()),
                ('img', models.ImageField(upload_to='images')),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
    ]
