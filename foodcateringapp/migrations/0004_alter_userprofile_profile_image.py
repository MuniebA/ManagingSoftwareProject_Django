# Generated by Django 4.2.7 on 2023-11-20 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodcateringapp', '0003_alter_userprofile_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_image',
            field=models.ImageField(default='Image/FEGCWHITE.png', upload_to='Image/'),
        ),
    ]
