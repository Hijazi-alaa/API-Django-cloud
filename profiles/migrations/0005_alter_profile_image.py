# Generated by Django 3.2.13 on 2022-05-10 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_w82a0x', upload_to='images/'),
        ),
    ]
