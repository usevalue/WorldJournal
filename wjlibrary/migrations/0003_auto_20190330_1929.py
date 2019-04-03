# Generated by Django 2.1.7 on 2019-03-30 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wjlibrary', '0002_author_fullname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='author',
            name='works',
        ),
        migrations.AddField(
            model_name='world',
            name='authors',
            field=models.ManyToManyField(to='wjlibrary.Author'),
        ),
    ]
