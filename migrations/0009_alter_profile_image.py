# Generated by Django 3.2.1 on 2022-10-27 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_profile_second_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default='C:\\\\Users\\\\SUVARNA\\\\Food_recommendation\\\\DJANGO\\\\minor\\\\media\\\\website\\\\images\\\\avtar.png', upload_to='website/images'),
        ),
    ]
