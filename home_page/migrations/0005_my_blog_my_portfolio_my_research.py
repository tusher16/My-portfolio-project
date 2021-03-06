# Generated by Django 3.2.4 on 2021-07-12 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_page', '0004_testiomonial'),
    ]

    operations = [
        migrations.CreateModel(
            name='My_blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(blank=True, max_length=300, null=True)),
                ('blog_short_dis', models.TextField(blank=True, max_length=600, null=True)),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('blog_readtime', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_publish_time', models.CharField(blank=True, max_length=100, null=True)),
                ('blog_medium_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='my_kaggle_link')),
            ],
        ),
        migrations.CreateModel(
            name='My_portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portfolio_title', models.CharField(blank=True, max_length=300, null=True)),
                ('portfolio_short_dis', models.TextField(blank=True, max_length=600, null=True)),
                ('portfolio_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('portfolio_readtime', models.CharField(blank=True, max_length=100, null=True)),
                ('portfolio_publish_time', models.CharField(blank=True, max_length=100, null=True)),
                ('portfolio_medium_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='my_kaggle_link')),
                ('portfolio_git_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='my_kaggle_link')),
            ],
        ),
        migrations.CreateModel(
            name='My_research',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('research_title', models.CharField(blank=True, max_length=300, null=True)),
                ('research_short_dis', models.TextField(blank=True, max_length=600, null=True)),
                ('research_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('research_readtime', models.CharField(blank=True, max_length=100, null=True)),
                ('research_published_by', models.CharField(blank=True, max_length=300, null=True)),
                ('research_publish_time', models.CharField(blank=True, max_length=100, null=True)),
                ('research_readmore_link', models.URLField(blank=True, db_index=True, max_length=128, unique=True, verbose_name='my_kaggle_link')),
            ],
        ),
    ]
