# Generated by Django 3.1 on 2020-08-22 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ddos', '0002_remove_profile_gender'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(default='avatar.png', upload_to='media/avatars/'),
        ),
    ]