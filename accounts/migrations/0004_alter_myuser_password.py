# Generated by Django 3.2.7 on 2021-09-07 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_myuser_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='password',
            field=models.CharField(max_length=128, verbose_name='password'),
        ),
    ]
