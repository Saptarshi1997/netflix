# Generated by Django 5.0.6 on 2024-08-13 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_profile_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(default='profile/default.jpg', upload_to='users/profile'),
        ),
    ]
