# Generated by Django 3.2.13 on 2022-05-10 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='../default_profile_txlx6h', upload_to='images/'),
        ),
    ]
