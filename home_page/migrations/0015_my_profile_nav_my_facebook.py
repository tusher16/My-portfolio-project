# Generated by Django 3.2.4 on 2021-07-13 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0014_auto_20210713_1416'),
    ]

    operations = [
        migrations.AddField(
            model_name='my_profile_nav',
            name='my_facebook',
            field=models.URLField(blank=True, db_index=True, max_length=128, verbose_name='my_facebook'),
        ),
    ]
