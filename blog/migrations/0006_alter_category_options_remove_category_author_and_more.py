# Generated by Django 4.0.3 on 2022-03-06 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_post_category_post_topics_alter_post_title_category'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={},
        ),
        migrations.RemoveField(
            model_name='category',
            name='author',
        ),
        migrations.RemoveField(
            model_name='category',
            name='content',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_posted',
        ),
        migrations.RemoveField(
            model_name='category',
            name='date_updated',
        ),
    ]
