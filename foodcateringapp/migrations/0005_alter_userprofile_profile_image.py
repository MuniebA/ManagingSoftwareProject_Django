# Generated by Django 4.2.7 on 2023-11-20 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcateringapp', '0004_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='FEGCWHITE.png', upload_to='Image/'),
        ),
    ]
