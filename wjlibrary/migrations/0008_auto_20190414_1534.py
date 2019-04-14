# Generated by Django 2.1.7 on 2019-04-14 19:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wjlibrary', '0007_auto_20190414_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='world',
            name='history_overview',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='world',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='wjlibrary.Author'),
        ),
        migrations.AlterField(
            model_name='world',
            name='purpose',
            field=models.TextField(null=True),
        ),
    ]