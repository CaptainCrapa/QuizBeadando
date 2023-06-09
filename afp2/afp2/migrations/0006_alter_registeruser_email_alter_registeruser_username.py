# Generated by Django 4.1.7 on 2023-04-05 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afp2', '0005_alter_registeruser_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registeruser',
            name='email',
            field=models.CharField(error_messages='Unique: Registration with this e-mail already exist!', max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='registeruser',
            name='username',
            field=models.CharField(error_messages='Unique: Registration with this e-mail already exist!', max_length=100, unique=True),
        ),
    ]
