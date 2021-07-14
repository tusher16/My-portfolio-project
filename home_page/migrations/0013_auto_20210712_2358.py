# Generated by Django 3.2.4 on 2021-07-12 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0012_auto_20210712_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='my_blog',
            name='blog_medium_link',
            field=models.URLField(blank=True, db_index=True, max_length=128, verbose_name='blog_medium_link'),
        ),
        migrations.AlterField(
            model_name='my_portfolio',
            name='portfolio_git_link',
            field=models.URLField(blank=True, db_index=True, max_length=128, verbose_name='portfolio_git_link'),
        ),
        migrations.AlterField(
            model_name='my_portfolio',
            name='portfolio_medium_link',
            field=models.URLField(blank=True, db_index=True, max_length=128, verbose_name='portfolio_medium_link'),
        ),
        migrations.AlterField(
            model_name='my_researche',
            name='research_publication_link',
            field=models.URLField(blank=True, db_index=True, max_length=128, verbose_name='research_publication_link'),
        ),
        migrations.AlterField(
            model_name='my_researche',
            name='research_readmore_link',
            field=models.URLField(blank=True, db_index=True, max_length=128, verbose_name='research_readmore_link'),
        ),
    ]